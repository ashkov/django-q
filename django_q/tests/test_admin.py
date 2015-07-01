from django.core.urlresolvers import reverse
from django.utils import timezone
from future.types.newstr import unicode

import pytest

from django_q import Task, schedule
from django_q.models import Failure


@pytest.mark.django_db
def test_admin_views(admin_client):
    s = schedule('sched.test')
    f = Task.objects.create(name='alfa-pappa-bravo-fail',
                            func='test.fail',
                            started=timezone.now(),
                            stopped=timezone.now(),
                            success=False)
    t = Task.objects.create(name='alfa-pappa-bravo-success',
                            func='test.succes',
                            started=timezone.now(),
                            stopped=timezone.now(),
                            success=True)
    admin_urls = (
        # schedule
        reverse('admin:django_q_schedule_changelist'),
        reverse('admin:django_q_schedule_add'),
        reverse('admin:django_q_schedule_change', args=(s.id,)),
        reverse('admin:django_q_schedule_history', args=(s.id,)),
        reverse('admin:django_q_schedule_delete', args=(s.id,)),
        # success
        reverse('admin:django_q_success_changelist'),
        reverse('admin:django_q_success_change', args=(t.id,)),
        reverse('admin:django_q_success_history', args=(t.id,)),
        reverse('admin:django_q_success_delete', args=(t.id,)),
        # failure
        reverse('admin:django_q_failure_changelist'),
        reverse('admin:django_q_failure_change', args=(f.id,)),
        reverse('admin:django_q_failure_history', args=(f.id,)),
        reverse('admin:django_q_failure_delete', args=(f.id,)),

    )
    for url in admin_urls:
        response = admin_client.get(url)
        assert response.status_code == 200

    # resubmit the failure
    url = reverse('admin:django_q_failure_changelist')
    data = {'action': 'retry_failed',
            '_selected_action': [f.pk]}
    response = admin_client.post(url, data)
    assert response.status_code == 302
    assert Failure.objects.filter(name=f.id).exists() is False
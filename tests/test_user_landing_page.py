from django.shortcuts import reverse
import pytest


@pytest.mark.parametrize("dues_amount", (3, 100))
def test_dues_amount_correct_after_logging_in(django_user_model, client, dues_amount):
    member = django_user_model.object.create(status="M", dues_amount=dues_amount)
    client.force_login(member)

    response = client.get(reverse("dues_landing_page"))

    assert dues_amount in response.content.decode()

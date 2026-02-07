
from django.core import mail
from django.template.loader import render_to_string
from django.conf import settings



class EmailService:
    @staticmethod
    def send_email(context: dict) -> None:
        html_context = render_to_string(
            template_name='emails/order.html',
            context=context
        )

        email = mail.EmailMultiAlternatives(
            subject="Order Creation",
            body="Order has been Created Successfully",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=["khalidbisimwa@gmail.com"],
        )

        # mail.send_mail(
        #     subject="Order Creation",
        #     message="Order has been Created Successfully",
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=['khalidbisimwa@gmail.com'],
        #     html_message=html_context
        # )

        email.attach_alternative(html_context, "text/html")
        email.send()

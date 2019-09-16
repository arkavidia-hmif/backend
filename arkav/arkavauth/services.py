from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils import timezone


class UserService:

    def send_email(self, user, subject, text_template, html_template):
        context = {
            'user': user,
            'token': user.token,
        }
        mail_text_message = text_template.render(context)
        mail_html_message = html_template.render(context)

        mail = EmailMultiAlternatives(
            subject=subject,
            body=mail_text_message,
            to=[user.email],
        )
        mail.attach_alternative(mail_html_message, 'text/html')
        mail.send()
        user.email_last_sent_at = timezone.now()
        user.save()

    def send_registration_confirmation_email(self, user):
        text_template = get_template('registration_confirmation_email.txt')
        html_template = get_template('registration_confirmation_email.html')

        self.send_email('[Arkavidia] Konfirmasi Email', text_template, html_template)
        user.confirmation_email_last_sent_time = timezone.now()
        user.save()

    def send_password_reset_email(self, password_reset_attempt):
        text_template = get_template('password_reset_confirmation_email.txt')
        html_template = get_template('password_reset_confirmation_email.html')

        user = password_reset_attempt.user
        self.send_email(user, '[Arkavidia] Reset Password', text_template, html_template)

        password_reset_attempt.sent_time = timezone.now()
        password_reset_attempt.save()

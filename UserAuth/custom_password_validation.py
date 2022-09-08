from django.utils.translation import ngettext
from django.core.exceptions import ValidationError


class MyCustomMinimumLengthValidator(object):
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    # silly, I know, but if your min length is one, put your message here
                    "پسورد انتخاب شده کوتاه است. طول پسورد باید %(min_length)d کاراکتر باشد.",
                    # if it's more than one (which it probably is) put your message here
                    "پسورد انتخاب شده کوتاه است. طول پسورد باید %(min_length)d کاراکتر باشد.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            # "Your password must contain at least %(min_length)d character.",
            # "Your password must contain at least %(min_length)d characters.",
            "",
            "",
            self.min_length
        ) % {'min_length': self.min_length}

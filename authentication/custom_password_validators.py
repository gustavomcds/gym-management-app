from django.utils.translation import gettext as _, ngettext
from django.contrib.auth.password_validation import (MinimumLengthValidator, UserAttributeSimilarityValidator, 
                                                     NumericPasswordValidator, CommonPasswordValidator)

import re
from difflib import SequenceMatcher
from django.core.exceptions import ValidationError, FieldDoesNotExist

class MinimumLengthValidatorPtBr(MinimumLengthValidator):

    def __init__(self):
        super().__init__()

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "A senha deve conter ao menos %(min_length)d caracteres",
                    "A senha deve conter ao menos %(min_length)d caracteres",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )
    
class UserAttributeSimilarityValidatorPtBr(UserAttributeSimilarityValidator):

    def __init__(self):
        super().__init__()

    def validate(self, password, user=None):
        if not user:
            return

        for attribute_name in self.user_attributes:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, str):
                continue
            value_parts = re.split(r'\W+', value) + [value]
            for value_part in value_parts:
                if SequenceMatcher(a=password.lower(), b=value_part.lower()).quick_ratio() >= self.max_similarity:
                    try:
                        verbose_name = str(user._meta.get_field(attribute_name).verbose_name)
                    except FieldDoesNotExist:
                        verbose_name = attribute_name
                    raise ValidationError(
                        _("A senha é muito semelhante a algum dos dados cadastrais"),
                        code='password_too_similar',
                        params={'verbose_name': verbose_name},
                    )

class NumericPasswordValidatorPtBr(NumericPasswordValidator):

    def __init__(self):
        super().__init__()

    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("A senha é completamente numérica"),
                code='password_entirely_numeric',
            )

class CommonPasswordValidatorPtBr(CommonPasswordValidator):

    def __init__(self):
        super().__init__()

    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                _("A senha é muito comum"),
                code='password_too_common',
            )
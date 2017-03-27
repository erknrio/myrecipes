# -*- coding: utf-8 -*-
# from django.http import Http404
from django.template import Library
from django.core.urlresolvers import reverse_lazy as reverse
from django.utils.safestring import mark_safe

register = Library()


@register.inclusion_tag('common/swiper-form-fields.html', takes_context=True)
def swiper_form(context):
    output_fields = context['form']
    return output_fields
    # return mark_safe(output_fields)
    # link = '<a href="{}" title="Página administrativa"><i class="glyphicon glyphicon-pencil"></i></a>'
    # if user.is_superuser:
    #     if isinstance(cosa, str):
    #         url = reverse(label, kwargs=kwargs)
    #     else:
    #         url = "admin:{}_{}_change".format(
    #             cosa.__class__._meta.app_label,
    #             cosa.__class__._meta.object_name.lower())
    #         url = reverse(url, args=[cosa.pk])
    #     return mark_safe(link.format(url))
    # else:
    #     return ""

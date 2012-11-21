from django.conf import settings

MASTER_CHECKBOX_GROUP_ATTR = getattr(settings,
        'CIROSANTILLI_MASTER_CHECKBOX_GROUP_ATTR',
        'master-group',
    )

SLAVE_CHECKBOX_GROUP_ATTR = getattr(settings,
        'CIROSANTILLI_SLAVE_CHECKBOX_GROUP_ATTR',
        'slave-of',
    )

CONTEXT = {
    'master_checkbox_group_attr':MASTER_CHECKBOX_GROUP_ATTR,
    'slave_checkbox_group_attr':SLAVE_CHECKBOX_GROUP_ATTR,
}

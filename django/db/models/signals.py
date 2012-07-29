from django.dispatch import Signal

class_prepared = Signal(providing_args=["class"])

pre_init = Signal(providing_args=["instance", "args", "kwargs"])
post_init = Signal(providing_args=["instance"])

pre_save = Signal(providing_args=["instance", "raw", "using", "update_fields"])
post_save = Signal(providing_args=["instance", "raw", "created", "using", "update_fields"])

pre_delete = Signal(providing_args=["instance", "using"])
post_delete = Signal(providing_args=["instance", "using"])

pre_syncdb = Signal(providing_args=["class", "app", "verbosity", "interactive", "type"])
post_syncdb = Signal(providing_args=["class", "app", "created_models", "verbosity", "interactive", "type"])

m2m_changed = Signal(providing_args=["action", "instance", "reverse", "model", "pk_set", "using"])

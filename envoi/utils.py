def add_from_namespace_to_dict_if_not_none(source_obj, source_key, target_obj, target_key):
    if hasattr(source_obj, source_key):
        value = getattr(source_obj, source_key)
        if value is not None:
            target_obj[target_key] = value

def make_module_dict(modules: list) -> dict:
    return {'!' + m.__name__[len(m.__package__)+1:]: m for m in modules}

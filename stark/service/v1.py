class StarkConfig(object):
    def __init__(self,model_class,site):
        self.model_class = model_class
        self.site = site


class StarkSite(object):

    def __init__(self):
        self._registry = {}

    def register(self,model_class,stark_config_class=None):
        if not stark_config_class:
            stark_config_class = StarkConfig
        self._registry[model_class] = stark_config_class(model_class,self)


site = StarkSite()




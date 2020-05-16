import requests, json

from kalliope.core.NeuronModule import (NeuronModule,
                                        MissingParameterException)
class Currency(NeuronModule):
    def __init__(self, **kwargs):
        super(Currency, self).__init__(**kwargs)
        # the args from the neuron configuration
        self.currency = kwargs.get('currency', None)

        # check if parameters have been provided
        if self._is_parameters_ok():

            result = dict()
            response = requests.get('https://api.hgbrasil.com/finance')
            result = response.json()
            result = result['results']['currencies']
            result = result[self.currency]
            self.say(result)

    def _is_parameters_ok(self):

        if self.currency is None:
            raise MissingParameterException("You must specify a currency")
        return True

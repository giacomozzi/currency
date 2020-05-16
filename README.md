Neuron name: Currency Quote

Installation:
  kalliope install --git-url https://github.com/giacomozzi/currency_quote

Synopsis: Description of the Neuron

Options: A table of the incoming parameters managed by the Neuron.

Return Values: A table of the returned values which can be catched by the say_template attribute.

Synapses example:

- name: "currency_quote"
    signals:
      - order: "Cotação do dólar"
    neurons:
      - currency_quote:
          currency: "USD"

          file_template: templates/currency.j2

Notes: Something which needs to be add.

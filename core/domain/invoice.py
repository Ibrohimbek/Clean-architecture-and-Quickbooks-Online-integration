from core.shared.domain_model import DomainModel


class Invoice:
    txn_id = ''
    txn_number = ''
    is_synced = None
    message = ''

    def __init__(self, uid, number, invoiced_date, order, customer, payment_term, **kwargs):
        self.uid = uid
        self.number = number
        self.invoiced_date = invoiced_date
        self.order = order
        self.customer = customer
        self.payment_term = payment_term

        self.txn_id = kwargs.get('txn_id', '')
        self.txn_number = kwargs.get('txn_number', '')
        self.is_synced = kwargs.get('is_synced')
        self.message = kwargs.get('message', '')

    @classmethod
    def from_dict(cls, adict):
        invoice = Invoice(
            uid=adict.get('uid'),
            number=adict.get('number'),
            invoiced_date=adict.get('invoiced_date'),
            order=adict.get('order'),
            customer=adict.get('customer'),
            payment_term=adict.get('payment_term'),
        )

        return invoice

DomainModel.register(Invoice)

    # def validate(self):
    #     pass
    #
    # @property
    # def total_price(self):
    #     pass
    #
    # @total_price.setter
    # def total_price(self, price):
    #     pass

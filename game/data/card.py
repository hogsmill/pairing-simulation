
class Card:

  def prepare_card(self, card):
    card['assigned'] = []
    card['remaining'] = card['level']
    card['completed'] = 0

    return card

  def card_is_complete(self, card):
    return card['completed'] >= card['level']

  def complete_work_on_card(self, card, amount, max_amount):
    amount = min(amount, max_amount)
    card['completed'] = card['completed'] + amount
    card['remaining'] = card['remaining'] - amount

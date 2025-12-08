def el_price(senti_per_kwh: float) -> float:
    """
    Print the price of electricity. Convert sents per kwh to euros per MWh.

    :param senti_per_kwh:
    :return: price in euros per MWh
    """
    return senti_per_kwh * 10


def banner(sentence: str) -> str:
    """Take given slogan and print it upper given number of times."""
    return sentence.upper()


def calculate_budget(guests: int) -> int:
    """Calculate party budget. Place costs 55 + 10 for each guest."""
    place_price = 55
    price_per_guest = 10
    return place_price + price_per_guest * guests


if __name__ == '__main__':
    senti = float(input("Sisesta elektrihind sentides kilovatt-tunni kohta: "))
    eur_per_MWh = el_price(senti)
    print(f"{senti} s/kwh on {eur_per_MWh} €/MWh")


    repeat_count = int(input("Mitu korda soovid sentence`it korrata? "))
    sentence = input("Milline on sinu sentence? ")
    banner_text = banner(sentence)
    print(f"{banner_text}\n" * repeat_count)


    invited_guests = int(input("Mitu inimest on peole kutsutud? "))
    confirmed_guests = int(input("Mitu inimest tuleb? "))
    min_budget = calculate_budget(confirmed_guests)
    max_budget = calculate_budget(confirmed_guests)
    print(f"Maksimaalne eelarve on {max_budget} eurot")
    print(f"Minimaalne eelarve on {min_budget} eurot")

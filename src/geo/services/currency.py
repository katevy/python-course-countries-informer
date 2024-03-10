from geo.clients.currency import CurrencyClient
from geo.clients.shemas import CurrencyRatesDTO


class CurrencyService:
    """
    Сервис для работы с данными о валюте.
    """

    def get_currency(
        self,
        base: str,
    ) -> CurrencyRatesDTO | None:
        """
        Получение курса валюты.
        :param country: Страна
        :return:
        """

        data = CurrencyClient().get_rates(base)
        if data:
            return CurrencyRatesDTO(
                base=data["base"],
                date=data["date"],
                rates=data["rates"],
            )

        return None

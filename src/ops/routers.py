from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist

from src.ops.models import Tariff, Calculation


router = APIRouter()


@router.get("/")
async def get_tariffs():
    tariffs = await Tariff.all()
    return tariffs


@router.get("/calculation")
async def calculate_insurance_cost(declared_value: float, cargo_type: str):
    # Ищем актуальный тариф по типу груза и текущей дате
    try:
        tariff = await Tariff.get(cargo_type=cargo_type)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Tariff not found")

    # Выполняем расчет стоимости страхования
    insurance_cost = declared_value * float(tariff.rate)

    # Сохраняем данные о расчете в базе данных
    calculation = Calculation(
        declared_value=declared_value,
        cargo_type=cargo_type,
        date=datetime.utcnow(),
        insurance_cost=insurance_cost
    )
    await calculation.save()

    # Возвращаем результат в формате JSON
    return {"insurance_cost": insurance_cost}


@router.post("/tariffs")
async def upload_tariffs(tariffs: List[dict]):
    # Удаляем все старые тарифы
    await Tariff.all().delete()

    # Загружаем новые тарифы
    for tariff_data in tariffs:
        tariff = Tariff(**tariff_data)
        await tariff.save()

    return {"message": "Tariffs uploaded successfully"}

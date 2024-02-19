import asyncio

from flask import request, abort, jsonify, Response

from app import app
from app.models import User
from app.weather import fetch_weather


async def update_balance_task(user_id: int, city: str):
    try:
        user = await User.get_user_by_id(user_id)
        temperature = await fetch_weather(city)
        new_balance = max(0, user[2] + round(temperature, 2))
        await User.update_balance(user_id, new_balance)
    except ValueError as e:
        abort(404, str(e))


@app.route('/update_user_balance', methods=['POST'])
def update_user_balance():
    try:
        user_id = request.json.get('userId')
        city = request.json.get('city')
        if not user_id or not city:
            abort(400, "userId and city must be provided")
        asyncio.run(update_balance_task(int(user_id), city))
        return Response(status=204)

    except ValueError as e:
        abort(404, str(e))


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found', 'message': error.description}), 404


@app.errorhandler(400)
def not_found_error(error):
    return jsonify({'error': 'Bad Request', 'message': error.description}), 400

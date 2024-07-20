# funciones para el endpoint pokemon

def pokemon_endpoint(pokemon_id):
    """
    Funcionalidad del endpoint para recibir info de pokemones
    """
    # revisando a través del argumento pokemon_if
    if not pokemon_id:
        # revisando el limit definido por el usuario
        limit = request.args.get('limit', None)
        offset = request.args.get('offset', None)
        # armando la query con los datos de los query params
        request_url = "{}?{}&{}".format(
            POKEAPI_URL,
            "limit={}".format(limit) if limit else "",
            "offset={}".format(offset) if offset else "")
        # haciendo la petición al api de pokeapi
        poke_response = requests.get(request_url).json()

        # procesando las strings de control para la paginación
        next_string = "{}://{}/pokemon?{}".format(
            request.scheme,
            request.host,
            poke_response["next"][poke_response["next"].index("offset"):]
            ) if poke_response["next"] else None
        previous_string = "{}://{}/pokemon?{}".format(
            request.scheme,
            request.host,
            poke_response["previous"][poke_response["previous"].index(
                "offset"):]
            ) if poke_response["previous"] else None
        # armando la respuesta
        return jsonify({
            "total": poke_response["count"],
            "control": {
                "siguiente": next_string,
                "anterior": previous_string
            },
            "resultados": [
                {
                    # recuperando solo el id del pokemon
                    "id": int(pokemon["url"][:-1].split('/')[-1]),
                    # recuperando el nombre del pokemon
                    "nombre": pokemon["name"]
                } for pokemon in poke_response["results"]
            ]
        })
    # Si hay un id definido se regresa la info detallada
    request_url = "{}/{}".format(
        POKEAPI_URL,
        pokemon_id
    )
    poke_response = requests.get(request_url)
    # validando que la respuesta sea exitosa
    # en caso contrario se levanta una excepción
    if poke_response.status_code != 200:
        abort(
            poke_response.status_code,
            description="Pokemon no encontrado")
    return poke_response.json()
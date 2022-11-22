import pandas as pd
import json

class ActorRepositories:
    def findActor(actor_id: int):
        raw_actor_data = pd.read_csv("data/credits.csv")
        actor_detail = raw_actor_data[["cast"]]
        json_actor_detail = [_cast for _cast in actor_detail['cast']][0].replace("\'", "\"").replace('None', '"None"')
        json_actor_detail = json.loads(json_actor_detail)
        result = list(filter(lambda actor: actor['id'] == actor_id, json_actor_detail))
        return result
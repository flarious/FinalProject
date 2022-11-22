from src.logics.actorBusinessLogics import ActorBusinessLogics

class ActorController:
    def findActor(actor_id: int):
        return ActorBusinessLogics.findActor(actor_id)
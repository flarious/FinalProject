from src.repositories.actorRepositories import ActorRepositories

class ActorBusinessLogics:
    def findActor(actor_id: int):
        return ActorRepositories.findActor(actor_id)
from treasury_prime_py.models.base import Base


class Simulation(Base):
    _API_PATH = "/simulation"

    @classmethod
    def get(
        cls, client=None, page_cursor=None, page_size=None, from_date=None, to_date=None
    ):
        raise NotImplementedError("Simulation objects are not instantiated.")

    @classmethod
    def get_by_id(cls, _id, client=None):
        raise NotImplementedError("Simulation objects are not instantiated.")

    @classmethod
    def random_simulation_body(cls, *args, **kwargs):
        raise NotImplementedError("Only called from Simulation child classes.")

    @classmethod
    def random_body(cls, simulation_type=None, **kwargs):
        if simulation_type is None:
            raise ValueError("simulation_type is required")
        return {
            "type": str(simulation_type),
            "simulation": cls.random_simulation_body(**kwargs),
        }

    @classmethod
    def fake_id(cls):
        raise NotImplementedError("Simulation objects are not instantiated.")

    @classmethod
    def create(cls, with_request=True, **kwargs):
        if with_request:
            return super(Simulation, cls).create(with_request=with_request, **kwargs)
        else:
            raise NotImplementedError("Simulations cannot be used locally.")

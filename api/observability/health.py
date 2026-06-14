from dataclasses import dataclass, asdict

@dataclass
class HealthStatus:
    status: str

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def ok(cls):
        return cls("OK")


class HealthCheck:

    @staticmethod
    def get_status() -> HealthStatus:
        return HealthStatus.ok()

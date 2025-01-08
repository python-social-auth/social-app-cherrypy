"""Flask SQLAlchemy ORM models for Social Auth"""

import cherrypy
from social_core.utils import module_member, setting_name
from social_sqlalchemy.storage import (
    BaseSQLAlchemyStorage,
    SQLAlchemyAssociationMixin,
    SQLAlchemyNonceMixin,
    SQLAlchemyPartialMixin,
    SQLAlchemyUserMixin,
)
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class SocialBase(DeclarativeBase):
    pass


DB_SESSION_ATTR = cherrypy.config.get(setting_name("DB_SESSION_ATTR"), "db")
UID_LENGTH = cherrypy.config.get(setting_name("UID_LENGTH"), 255)
User = module_member(cherrypy.config[setting_name("USER_MODEL")])


class CherryPySocialBase:
    @classmethod
    def _session(cls):
        return getattr(cherrypy.request, DB_SESSION_ATTR)


class UserSocialAuth(CherryPySocialBase, SQLAlchemyUserMixin, SocialBase):
    """Social Auth association model"""

    uid: Mapped[str] = mapped_column(String(UID_LENGTH))
    user_id: Mapped[int] = mapped_column(
        ForeignKey(User.id), nullable=False, index=True
    )
    user: Mapped["User"] = relationship(User, backref="social_auth")

    @classmethod
    def username_max_length(cls):
        return User.__table__.columns.get("username").type.length

    @classmethod
    def user_model(cls):
        return User


class Nonce(CherryPySocialBase, SQLAlchemyNonceMixin, SocialBase):
    """One use numbers"""

    pass


class Association(CherryPySocialBase, SQLAlchemyAssociationMixin, SocialBase):
    """OpenId account association"""

    pass


class Partial(CherryPySocialBase, SQLAlchemyPartialMixin, SocialBase):
    """Partial pipeline storage"""

    pass


class CherryPyStorage(BaseSQLAlchemyStorage):
    user = UserSocialAuth
    nonce = Nonce
    association = Association
    partial = Partial

from sqlalchemy import Column, Text, Float, text, Integer
from clickhouse_sqlalchemy import engines
from clickhouse_sqlalchemy.types.common import DateTime, UUID, Nullable
from sqlalchemy.ext.declarative import declared_attr
from fastapi_utils.camelcase import camel2snake

from app.orm.base.main import Base
from app.orm.cfg.engine import ORMEngine


class pitUsers(Base):

    @declared_attr
    def __tablename__(cls) -> str:
        return camel2snake(cls.__name__)

    @declared_attr
    def __table_args__(cls):
        return engines.MergeTree(order_by=['pit_users_uuid']), {'schema': ORMEngine.DB_NAME}

    pit_user_uuid = Column(UUID, primary_key=True, server_default=text("generateUUIDv4()"))

    h_source = Column(Text)
    h_endpoint = Column(Text)

    pit_id = Column(Nullable(Integer))
    pit_uid = Column(Nullable(Text))
    pit_password = Column(Nullable(Text))
    pit_first_name = Column(Nullable(Text))
    pit_last_name = Column(Nullable(Text))
    pit_username = Column(Nullable(Text))
    pit_email = Column(Nullable(Text))
    pit_avatar = Column(Nullable(Text))
    pit_gender = Column(Nullable(Text))
    pit_phone_number = Column(Nullable(Text))
    pit_social_insurance_number = Column(Nullable(Integer))
    pit_date_of_birth = Column(Nullable(DateTime))
    pit_employment_title = Column(Nullable(Text))
    pit_employment_key_skill = Column(Nullable(Text))
    pit_address_city = Column(Nullable(Text))
    pit_address_street_name = Column(Nullable(Text))
    pit_address_street_address = Column(Nullable(Text))
    pit_address_zip_code = Column(Nullable(Integer))
    pit_address_state = Column(Nullable(Text))
    pit_address_country = Column(Nullable(Text))
    pit_address_coordinates_lat = Column(Nullable(Float))
    pit_address_coordinates_lng = Column(Nullable(Float))
    pit_credit_card_cc_number = Column(Nullable(Integer))
    pit_subscription_plan = Column(Nullable(Text))
    pit_subscription_status = Column(Nullable(Text))
    pit_subscription_payment_method = Column(Nullable(Text))
    pit_subscription_term = Column(Nullable(Text))

    pit_ts = Column(DateTime)

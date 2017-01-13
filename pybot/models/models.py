from peewee import *

mysql_dl = MySQLDatabase('demo', password='root', user='root')

class BaseModel(Model):
  class Meta:
    database = mysql_dl

class Entity(BaseModel):
  name = CharField(unique=True)
  type = CharField()
  color = CharField()
  userId = CharField()
  id = FixedCharField(max_length=36, primary_key=True)
  createdAt = BigIntegerField()
  updatedAt = BigIntegerField()

class Expression(BaseModel):
  id = FixedCharField(max_length=36, primary_key=True)
  sentence = FixedCharField()
  createdAt = BigIntegerField()
  updatedAt = BigIntegerField()

class InlineEntity(BaseModel):
  id = FixedCharField(max_length=36)
  createdAt = BigIntegerField()
  updatedAt = BigIntegerField()
  start = IntegerField()
  end = IntegerField()
  entity = ForeignKeyField(Entity, related_name='inlineEntities', db_column='entityId')
  expression = ForeignKeyField(Expression, related_name='InlineEntities', db_column='expressionId')

if __name__ == '__main__':
  query = InlineEntity.select()

  for inlineEntity in query:
    print inlineEntity.entity.name
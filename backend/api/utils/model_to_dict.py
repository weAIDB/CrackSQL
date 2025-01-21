from datetime import datetime as cdatetime  # 有时候会返回datatime类型
from datetime import date, time
from models import BaseModel as Model
from sqlalchemy.orm import class_mapper
from config.db_config import db


def query_to_dict(models):
    if isinstance(models, list):
        if len(models) == 0:
            return []
        if isinstance(models[0], Model):
            lst = []
            for model in models:
                dit = model_to_dict(model)
                lst.append(dit)
            return lst
        else:
            res = result_to_dict(models)
            return res
    else:
        if isinstance(models, Model):
            dit = model_to_dict(models)
            return dit
        else:
            res = dict(zip(models.keys(), models))
            find_datetime(res)
            return res


# 当结果为result对象列表时，result有key()方法
def result_to_dict(results):
    res = [dict(zip(r.keys(), r)) for r in results]
    # 这里r为一个字典，对象传递直接改变字典属性
    for r in res:
        find_datetime(r)
    return res


def model_to_dict(obj, visited_children=None, back_relationships=None):
    if visited_children is None:
        visited_children = set()
    if back_relationships is None:
        back_relationships = set()
    serialized_data = {c.key: getattr(obj, c.key)
                       for c in obj.__table__.columns}
    relationships = class_mapper(obj.__class__).relationships
    visitable_relationships = [
        (name,
         rel) for name,
        rel in relationships.items() if name not in back_relationships]
    for name, relation in visitable_relationships:
        if relation.backref:
            back_relationships.add(relation.backref)
        relationship_children = getattr(obj, name)
        if relationship_children is not None:
            if relation.uselist:
                children = []
                for child in [
                        c for c in relationship_children if c not in visited_children]:
                    visited_children.add(child)
                    children.append(
                        model_to_dict(
                            child,
                            visited_children,
                            back_relationships))
                serialized_data[name] = children
            else:
                serialized_data[name] = model_to_dict(
                    relationship_children, visited_children, back_relationships)
    return serialized_data


def find_datetime(value):
    for v in value:
        if (isinstance(value[v], cdatetime)):
            value[v] = convert_datetime(value[v])  # 这里原理类似，修改的字典对象，不用返回即可修改


def convert_datetime(value):
    if value:
        if (isinstance(value, (cdatetime, db.DateTime))):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        elif (isinstance(value, (date, db.Date))):
            return value.strftime("%Y-%m-%d")
        elif (isinstance(value, (db.Time, time))):
            return value.strftime("%H:%M:%S")
    else:
        return ""

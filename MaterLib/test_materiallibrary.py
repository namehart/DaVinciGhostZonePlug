import pytest
import MaterLib as ML
import sqlalchemy

sqlalchemy.create_engine("sqlite:///example.db")


def test_init():
    ML.letit_go(r"\testshili\bilibili_BV1yx411A72S_MP3.mp4")

    ML.letit_go(r"\testshili\吒儿.flac", local=True)

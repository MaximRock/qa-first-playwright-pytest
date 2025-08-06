from typing import Any

from data.assertions import Assertions
from data.data_for_tests import DataForTests
from data.environment import Environment
from data.generator import Generator
from data.parametr_pairs import ParametrPairs

host: str = Environment().get_base_url()
gen: str = Generator()
testdata: list[tuple[Any, ...]] = ParametrPairs().testdata()
data_for_tests = DataForTests()
assertion = Assertions()

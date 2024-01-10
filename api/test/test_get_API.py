from api.operation.get_API import read_root

def test_get_population_density_success():
    assert read_root()
    
def test_get_population_density_not_none():
    countries = read_root()
    assert countries != None

def test_get_population_density_has_elemnests():
    countries = read_root()
    assert len(countries) > 0

def test_get_population_density_length():
    countries = read_root()
    assert len(countries) == 5

def test_get_population_density_check_elements_length():
    countries = read_root()
    for countrie in countries:
        assert len(countrie) > 0 
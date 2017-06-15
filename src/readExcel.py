import xlrd
from zipfile import ZipFile
import pprint

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet    = workbook.sheet_by_index(0)

    dados = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    custo    = sheet.col_values(1, start_rowx=1, end_rowx=None)
    maxValor = max(custo)
    minValor = min(custo)

    maxPosicao = custo.index(maxValor) + 1
    minPosicao = custo.index(minValor) + 1

    maxDataHora       = sheet.cell_value(maxPosicao, 0)
    maxDataHoraAsDate = xlrd.xldate_as_tuple(maxDataHora, 0)
    minDataHora       = sheet.cell_value(minPosicao, 0)
    minDataHoraAsDate = xlrd.xldate_as_tuple(minDataHora, 0)
    data = {
            'maxtime': maxDataHoraAsDate,
            'maxvalue': maxValor,
            'mintime': minDataHoraAsDate,
            'minvalue': minValor,
            'avgcoast': sum(custo) / float(len(custo))
    }
    return data

datafile = "../data/2013_ERCOT_Hourly_Load_Data.xls"
#open_zip(datafile)
data = parse_file(datafile)

print data

pprint.pprint(data)
assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
assert round(data['maxvalue'], 10) == round(18779.02551, 10)

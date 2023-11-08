import datetime

import pandas
import pandas as pd
from PySide6.QtWidgets import QTableWidget, QMessageBox, QTableWidgetItem

from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.uniforme_repository import UniformeRepository
from infra.repository.funcionario_repository import FuncionarioRepository


class MainWindowService:

    def __init__(self):
        self.emprestimo_repository = EmprestimoRepository()
        self.funcionario_repository = FuncionarioRepository()
        self.uniforme_repository = UniformeRepository()

    def populate_table_funcionario(self, main_window):
        main_window.tb_funcionario.setRowCount(0)
        lista_funcionarios = self.funcionario_repository.select_all_funcionario()
        for funcionario in lista_funcionarios[:]:  # lista espelho para iteração
            if not funcionario.ativo:
                lista_funcionarios.remove(funcionario)
        main_window.tb_funcionario.setRowCount(len(lista_funcionarios))
        for linha, funcionario in enumerate(lista_funcionarios):
            if funcionario.ativo:
                main_window.tb_funcionario.setItem(linha, 0, funcionario.nome)
                main_window.tb_funcionario.setItem(linha, 1, funcionario.cpf)

    def populate_table_uniforme(self, main_window):
        main_window.tb_uniforme.setRowCount(0)
        lista_uniforme = self.uniforme_repository.select_all_uniformes()
        for uniforme in lista_uniforme[:]:
            if not uniforme.ativo:
                lista_uniforme.remove(uniforme)
        main_window.tb_uniforme.setRowCount(len(lista_uniforme))
        for linha, uniforme in enumerate(lista_uniforme):
            if uniforme.ativo:
                main_window.tb_uniforme.setItem(linha, 0, uniforme.nome)

    def populate_emprestimos_ativos(self, main_window):
        main_window.tb_emprestimos_ativos.setRowCount(0)
        emprestimos_ativos = self.emprestimo_repository.select_emprestimos_ativos()
        main_window.tb_emprestimos_ativos.setRowCount(len(emprestimos_ativos))
        for linha, (emp,funcionario, uniforme) in enumerate(emprestimos_ativos):
            main_window.tb_emprestimos_ativos.setItem(linha, 0, funcionario.nome)
            main_window.tb_emprestimos_ativos.setItem(linha, 1, funcionario.cpf)
            main_window.tb_emprestimos_ativos.setItem(linha, 2, emp.data_emprestimo.strftime('%d/%m/%Y'))
            main_window.tb_emprestimos_ativos.setItem(linha, 3, uniforme.nome)

    def populate_combo_uniformes(self, emprestimo_ui):
        emprestimo_ui.cb_uniforme.clear()
        emprestimo_ui.cb_uniforme.addItem('Selecione um item')
        emprestimo_ui.uniformes = self.uniforme_repository.select_all_uniformes()
        for uniforme in emprestimo_ui.uniformes[:]:
            if not uniforme.ativo:
                emprestimo_ui.uniformes.remove(uniforme)
        for uniforme in emprestimo_ui.uniformes:
            emprestimo_ui.cb_uniforme.addItem(uniforme.nome)

    def populate_relatorio(self, main_window):
        try:
            main_window.tb_relatorio.setRowCount(0)
            emprestimos = self.emprestimo_repository.select_emprestimos_in_period(main_window.txt_data_inicial.text(),
                                                                                  main_window.txt_data_final.text())
            main_window.tb_relatorio.setRowCount(len(emprestimos))
            for linha, (emp, funcionario, uniforme) in enumerate(emprestimos):
                main_window.tb_relatorio.setItem(linha, 0, QTableWidgetItem(funcionario.nome))
                main_window.tb_relatorio.setItem(linha, 1, QTableWidgetItem(funcionario.cpf))
                main_window.tb_relatorio.setItem(linha, 2, QTableWidgetItem(emp.data_emprestimo.strftime('%d/%m/%Y')))
                main_window.tb_relatorio.setItem(linha, 3, QTableWidgetItem(uniforme.nome))
        except Exception as e:
            QMessageBox.warning(main_window, 'Atenção', f'Período de data incorreto! \nErro {e}')

    def export_relatorio(self, main_window):
        if main_window.tb_relatorio.rowCount() > 0:
            rows = main_window.tb_relatorio.rowCount()
            cols = main_window.tb_relatorio.columnCount()
            headers = ['Nonme do funcionário', 'CPF do funcionário', 'Data de empréstimo', 'Data de devolução',
                       'Tipo de uniforme']
            data = []
            for row in range(rows):
                row_data = []
                for col in range(cols):
                    item = main_window.tb_relatorio.item(row, col)
                    if item and item.text():
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                data.append(row_data)
            df = pandas.DataFrame(data, columns=headers)
        try:
            df.to_excel(f'relatorio_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx', index=False)
            QMessageBox.information(main_window, 'Empréstimos', f'Relatório gerado com sucesso!')
        except Exception as e:
            QMessageBox.warning(main_window, 'Atenção', f'Erro ao gerar relatório! \nErro {e}')


#TODO fazer algo

import os

os.getcwd()

os.chdir('files_location')

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


string_vector=['64','65', '66', '67', '68', '69', '70', '195', '196','208','210','212_01', '213', '214_00']

df_0=pd.read_csv('Teste_64.dat',sep=' ', header=None)

df_1=pd.read_csv('Teste_65.dat',sep=' ', header=None)

df_2=pd.read_csv('Teste_66.dat',sep=' ', header=None)

df_3=pd.read_csv('Teste_67.dat',sep=' ', header=None)

df_4=pd.read_csv('Teste_68.dat',sep=' ', header=None)

df_5=pd.read_csv('Teste_69.dat',sep=' ', header=None)

df_6=pd.read_csv('Teste_70.dat',sep=' ', header=None)

df_7=pd.read_csv('Teste_195.dat',sep=' ', header=None)

df_8=pd.read_csv('Teste_196.dat',sep=' ', header=None)

df_9=pd.read_csv('Teste_208.dat',sep=' ', header=None)

df_10=pd.read_csv('Teste_210.dat',sep=' ', header=None)

df_11=pd.read_csv('Teste_212_01.dat',sep=' ', header=None)

df_12=pd.read_csv('Teste_213.dat',sep=' ', header=None)

df_13=pd.read_csv('Teste_214_00.dat',sep=' ', header=None)

tabs=['df_0', 'df_1', 'df_2', 'df_3', 'df_4', 'df_5','df_6', 'df_7', 'df_8', 'df_9', 'df_10', 'df_11', 'df_12','df_13']

Data_Number = 14

for i in range(0, Data_Number):
    if (i == 0):
        fig, ax = plt.subplots()
        ax.plot(df_0 [0], df_0[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 1):
        fig, ax = plt.subplots()
        ax.plot(df_1[0], df_1[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 2):
        fig, ax = plt.subplots()
        ax.plot(df_2[0], df_2[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 3):
        fig, ax = plt.subplots()
        ax.plot(df_3[0], df_3[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 4):
        fig, ax = plt.subplots()
        ax.plot(df_4[0], df_4[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 5):
        fig, ax = plt.subplots()
        ax.plot(df_5[0], df_5[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 6):
        fig, ax = plt.subplots()
        ax.plot(df_6 [0], df_6[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 7):
        fig, ax = plt.subplots()
        ax.plot(df_7[0], df_7[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 8):
        fig, ax = plt.subplots()
        ax.plot(df_8[0], df_8[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 9):
        fig, ax = plt.subplots()
        ax.plot(df_9[0], df_9[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 10):
        fig, ax = plt.subplots()
        ax.plot(df_10[0], df_10[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 11):
        fig, ax = plt.subplots()
        ax.plot(df_11[0], df_11[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 12):
        fig, ax = plt.subplots()
        ax.plot(df_12[0], df_12[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()
    if (i == 13):
        fig, ax = plt.subplots()
        ax.plot(df_13[0], df_13[1])

        ax.set(xlabel='time', ylabel='freq',
               title=string_vector[i])
        ax.grid()

        fig.savefig('test_fig_' + string_vector[i] + '.png')
        plt.show()

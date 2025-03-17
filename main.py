import math
import streamlit as st
from openpyxl import load_workbook
st.set_page_config("Gearbox & Gearless Calculator", layout="wide")
wb = load_workbook('Data-Ranjbar-Gearbox&Gearless.xlsx')
with st.sidebar:
    st.title("تحلیل محاسبات موتور گیربکس و گیرلس")
cols = st.columns(3)
with cols[0]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb2 = ws['B2']
            cellc2 = ws['C2']
            celld2 = ws['D2']
            new_valueb2 = st.selectbox('نوع موتور', options=[cellc2.value, celld2.value],
                                       key=f'{cellb2.coordinate}_{sheet_name}')
            if new_valueb2 == cellc2.value:
                cellb2.value = cellc2.value
            elif new_valueb2 == celld2.value:
                cellb2.value = celld2.value
with cols[1]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb3 = ws['B3']
            cellc3 = ws['C3']
            celld3 = ws['D3']
            celle3 = ws['E3']
            cellf3 = ws['F3']
            cellg3 = ws['G3']
            cellh3 = ws['H3']
            celli3 = ws['I3']
            new_valueb3 = st.selectbox('ظرفیت (بر حسب نفر)', options=[cellc3.value, celld3.value, celle3.value, cellf3.value, cellg3.value, cellh3.value, celli3.value],
                                       key=f'{cellb3.coordinate}_{sheet_name}')
            if new_valueb3 == cellc3.value:
                cellb3.value = cellc3.value
            elif new_valueb3 == celld3.value:
                cellb3.value = celld3.value
            elif new_valueb3 == celle3.value:
                cellb3.value = celle3.value
            elif new_valueb3 == cellf3.value:
                cellb3.value = cellf3.value
            elif new_valueb3 == cellg3.value:
                cellb3.value = cellg3.value
            elif new_valueb3 == cellh3.value:
                cellb3.value = cellh3.value
            elif new_valueb3 == celli3.value:
                cellb3.value = celli3.value
with cols[2]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb4 = ws['B4']
            cellc4 = ws['C4']
            celld4 = ws['D4']
            celle4 = ws['E4']
            cellf4 = ws['F4']
            cellg4 = ws['G4']
            cellh4 = ws['H4']
            celli4 = ws['I4']
            cellj4 = ws['J4']
            cellk4 = ws['K4']
            celll4 = ws['L4']
            cellm4 = ws['M4']
            celln4 = ws['N4']
            cello4 = ws['O4']
            cellp4 = ws['P4']
            cellq4 = ws['Q4']
            cellr4 = ws['R4']
            if cellb2.value == cellc2.value:
                if cellb3.value == cellc3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[cellc4.value, celld4.value, celle4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == cellc4.value:
                        cellb4.value = cellc4.value
                    elif new_valueb4 == celld4.value:
                        cellb4.value = celld4.value
                    elif new_valueb4 == celle4.value:
                        cellb4.value = celle4.value
                elif cellb3.value == celld3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[celld4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == celld4.value:
                        cellb4.value = celld4.value
                elif cellb3.value == celle3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[celle4.value, cellf4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == celle4.value:
                        cellb4.value = celle4.value
                    elif new_valueb4 == cellf4.value:
                        cellb4.value = cellf4.value
                elif cellb3.value == cellf3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[celle4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == celle4.value:
                        cellb4.value = celle4.value
                elif cellb3.value == cellg3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[cellf4.value, cellg4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == cellf4.value:
                        cellb4.value = cellf4.value
                    elif new_valueb4 == cellg4.value:
                        cellb4.value = cellg4.value
                elif cellb3.value == cellh3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[cellf4.value, cellh4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == cellf4.value:
                        cellb4.value = cellf4.value
                    elif new_valueb4 == cellh4.value:
                        cellb4.value = cellh4.value
                elif cellb3.value == celli3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[cellg4.value, celli4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == cellg4.value:
                        cellb4.value = cellg4.value
                    elif new_valueb4 == celli4.value:
                        cellb4.value = celli4.value
            elif cellb2.value == celld2.value:
                if cellb3.value == cellc3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)',
                                               options=[cellj4.value, cellc4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == cellj4.value:
                        cellb4.value = cellj4.value
                    elif new_valueb4 == cellc4.value:
                        cellb4.value = cellc4.value
                elif cellb3.value == celld3.value or cellb3.value == celle3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[cellk4.value, cellm4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == cellk4.value:
                        cellb4.value = cellk4.value
                    elif new_valueb4 == cellm4.value:
                        cellb4.value = cellm4.value
                elif cellb3.value == cellf3.value or cellb3.value == cellg3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[celll4.value, cello4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == celll4.value:
                        cellb4.value = celll4.value
                    elif new_valueb4 == cello4.value:
                        cellb4.value = cello4.value
                elif cellb3.value == cellh3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[celln4.value, cellq4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == celln4.value:
                        cellb4.value = celln4.value
                    elif new_valueb4 == cellq4.value:
                        cellb4.value = cellq4.value
                elif cellb3.value == celli3.value:
                    new_valueb4 = st.selectbox('توان خروجی موتور (بر حسب کیلووات)', options=[cellp4.value, cellr4.value],
                                               key=f'{cellb4.coordinate}_{sheet_name}')
                    if new_valueb4 == cellp4.value:
                        cellb4.value = cellp4.value
                    elif new_valueb4 == cellr4.value:
                        cellb4.value = cellr4.value


cols = st.columns(3)
with cols[1]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb5 = ws['B5']
            cellc5 = ws['C5']
            celld5 = ws['D5']
            if cellb2.value == cellc2.value:
                if cellb3.value == cellc3.value:
                    new_valueb5 = st.selectbox('حداکثر سرعت (بر حسب متر بر ثانیه)',
                                               options=[cellc5.value, celld5.value],
                                               key=f'{cellb5.coordinate}_{sheet_name}')
                    if new_valueb5 == cellc5.value:
                        cellb5.value = cellc5.value
                    elif new_valueb5 == celld5.value:
                        cellb5.value = celld5.value
                elif cellb3.value == celld3.value:
                    new_valueb5 = st.selectbox('حداکثر سرعت (بر حسب متر بر ثانیه)',
                                               options=[cellc5.value],
                                               key=f'{cellb5.coordinate}_{sheet_name}')
                    if new_valueb5 == cellc5.value:
                        cellb5.value = cellc5.value
                elif cellb3.value == celle3.value:
                    new_valueb5 = st.selectbox('حداکثر سرعت (بر حسب متر بر ثانیه)',
                                               options=[cellc5.value, celld5.value],
                                               key=f'{cellb5.coordinate}_{sheet_name}')
                    if new_valueb5 == cellc5.value:
                        cellb5.value = cellc5.value
                    elif new_valueb5 == celld5.value:
                        cellb5.value = celld5.value
                elif cellb3.value == cellf3.value:
                    new_valueb5 = st.selectbox('حداکثر سرعت (بر حسب متر بر ثانیه)',
                                               options=[cellc5.value],
                                               key=f'{cellb5.coordinate}_{sheet_name}')
                    if new_valueb5 == cellc5.value:
                        cellb5.value = cellc5.value
                elif cellb3.value == cellg3.value:
                    new_valueb5 = st.selectbox('حداکثر سرعت (بر حسب متر بر ثانیه)',
                                               options=[cellc5.value, celld5.value],
                                               key=f'{cellb5.coordinate}_{sheet_name}')
                    if new_valueb5 == cellc5.value:
                        cellb5.value = cellc5.value
                    elif new_valueb5 == celld5.value:
                        cellb5.value = celld5.value
                elif cellb3.value == cellh3.value:
                    new_valueb5 = st.selectbox('حداکثر سرعت (بر حسب متر بر ثانیه)',
                                               options=[cellc5.value, celld5.value],
                                               key=f'{cellb5.coordinate}_{sheet_name}')
                    if new_valueb5 == cellc5.value:
                        cellb5.value = cellc5.value
                    elif new_valueb5 == celld5.value:
                        cellb5.value = celld5.value
                elif cellb3.value == celli3.value:
                    new_valueb5 = st.selectbox('حداکثر سرعت (بر حسب متر بر ثانیه)',
                                               options=[cellc5.value, celld5.value],
                                               key=f'{cellb5.coordinate}_{sheet_name}')
                    if new_valueb5 == cellc5.value:
                        cellb5.value = cellc5.value
                    elif new_valueb5 == celld5.value:
                        cellb5.value = celld5.value
            elif cellb2.value == celld2.value:
                new_valueb5 = st.selectbox('حداکثر سرعت (بر حسب متر بر ثانیه)',
                                           options=[cellc5.value, celld5.value],
                                           key=f'{cellb5.coordinate}_{sheet_name}')
                if new_valueb5 == cellc5.value:
                    cellb5.value = cellc5.value
                elif new_valueb5 == celld5.value:
                    cellb5.value = celld5.value

if st.button('ثبت'):
    ws1 = wb['Data (1)']
    ws2 = wb['Data (2)']
    if ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['C3'].value and ws1['B4'].value == ws1['C4'].value:
        MotorDescription = f"""
        <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A2'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A2'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['C3'].value and ws1['B4'].value == ws1['D4'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A3'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A3'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['D3'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A4'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A4'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['C3'].value and ws1['B5'].value == ws1['D5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A5'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A5'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['E3'].value and ws1['B5'].value == ws1['C5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A6'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A6'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['E3'].value and ws1['B5'].value == ws1['D5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A7'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A7'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['F3'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A8'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A8'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['G3'].value and ws1['B5'].value == ws1['C5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A9'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A9'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['G3'].value and ws1['B5'].value == ws1['D5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A10'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A10'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['H3'].value and ws1['B5'].value == ws1['C5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A11'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A11'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['H3'].value and ws1['B5'].value == ws1['D5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A12'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A12'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['I3'].value and ws1['B5'].value == ws1['C5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A13'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A13'].value
    elif ws1['B2'].value == ws1['C2'].value and ws1['B3'].value == ws1['I3'].value and ws1['B5'].value == ws1['D5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A14'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A14'].value
    elif ws1['B2'].value == ws1['D2'].value and ws1['B3'].value == ws1['C3'].value and ws1['B5'].value == ws1['C5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A16'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A16'].value
    elif ws1['B2'].value == ws1['D2'].value and ws1['B3'].value == ws1['C3'].value and ws1['B5'].value == ws1['D5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A17'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A17'].value
    elif ws1['B2'].value == ws1['D2'].value and (ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value) and ws1['B5'].value == ws1['C5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A18'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A18'].value
    elif ws1['B2'].value == ws1['D2'].value and (ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value) and ws1['B5'].value == ws1['D5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A19'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A19'].value
    elif ws1['B2'].value == ws1['D2'].value and (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value) and ws1['B5'].value == ws1['C5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A20'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A20'].value
    elif ws1['B2'].value == ws1['D2'].value and (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value) and ws1['B5'].value == ws1['D5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A21'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A21'].value
    elif ws1['B2'].value == ws1['D2'].value and (ws1['B3'].value == ws1['H3'].value) and ws1['B5'].value == ws1['C5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A22'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A22'].value
    elif ws1['B2'].value == ws1['D2'].value and (ws1['B3'].value == ws1['H3'].value) and ws1['B5'].value == ws1['D5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A23'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A23'].value
    elif ws1['B2'].value == ws1['D2'].value and (ws1['B3'].value == ws1['I3'].value) and ws1['B5'].value == ws1['C5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A24'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A24'].value
    elif ws1['B2'].value == ws1['D2'].value and (ws1['B3'].value == ws1['I3'].value) and ws1['B5'].value == ws1['D5'].value:
        MotorDescription = f"""
        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A25'].value}</div>
        """
        st.markdown(MotorDescription, unsafe_allow_html=True)
        ws2['A1'].value = ws2['A25'].value
    cols = st.columns(2)
    with cols[0]:
        Description = f"""
                        <div  style='padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>مشخصات </div>
                        """
        st.markdown(Description, unsafe_allow_html=True)
    with cols[1]:
        QuantityDescription = f"""
                                <div  style='padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>مقدار</div>
                                """
        st.markdown(QuantityDescription, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            GearboxRatioDescription = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B1'].value}</div>
                                    """
            st.markdown(GearboxRatioDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            MaxAxleLoadDescription = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B15'].value}</div>
                                    """
            st.markdown(MaxAxleLoadDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            GearboxRatioQuantity = f"""
            <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B2'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B3'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B4'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B5'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B6'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B7'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B8'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B9'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B10'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B11'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B12'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B13'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            GearboxRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B14'].value}</div>
            """
            st.markdown(GearboxRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            MaxAxleLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B16'].value}</div>
            """
            st.markdown(MaxAxleLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            MaxAxleLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B17'].value}</div>
            """
            st.markdown(MaxAxleLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            MaxAxleLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B18'].value}</div>
            """
            st.markdown(MaxAxleLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            MaxAxleLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B19'].value}</div>
            """
            st.markdown(MaxAxleLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            MaxAxleLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B20'].value}</div>
            """
            st.markdown(MaxAxleLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            MaxAxleLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B21'].value}</div>
            """
            st.markdown(MaxAxleLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            MaxAxleLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B22'].value}</div>
            """
            st.markdown(MaxAxleLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            MaxAxleLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B23'].value}</div>
            """
            st.markdown(MaxAxleLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            MaxAxleLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B24'].value}</div>
            """
            st.markdown(MaxAxleLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            MaxAxleLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B25'].value}</div>
            """
            st.markdown(MaxAxleLoadQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            MaxStaticLoadDescription = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C1'].value}</div>
                                    """
            st.markdown(MaxStaticLoadDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            RatedTorqueDescription = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C15'].value}</div>
                                                """
            st.markdown(RatedTorqueDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C2'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C3'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C4'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C5'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C6'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C7'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C8'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C9'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C10'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C11'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C12'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C13'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            MaxStaticLoadQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C14'].value}</div>
            """
            st.markdown(MaxStaticLoadQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            RatedTorqueQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C16'].value}</div>
            """
            st.markdown(RatedTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            RatedTorqueQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C17'].value}</div>
            """
            st.markdown(RatedTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            RatedTorqueQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C18'].value}</div>
            """
            st.markdown(RatedTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            RatedTorqueQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C19'].value}</div>
            """
            st.markdown(RatedTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            RatedTorqueQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C20'].value}</div>
            """
            st.markdown(RatedTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            RatedTorqueQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C21'].value}</div>
            """
            st.markdown(RatedTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            RatedTorqueQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C22'].value}</div>
            """
            st.markdown(RatedTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            RatedTorqueQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C23'].value}</div>
            """
            st.markdown(RatedTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            RatedTorqueQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C24'].value}</div>
            """
            st.markdown(RatedTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            RatedTorqueQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C25'].value}</div>
            """
            st.markdown(RatedTorqueQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            GearboxEfficiencyDescription = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D1'].value}</div>
                                    """
            st.markdown(GearboxEfficiencyDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            TractionRatioDescription = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D15'].value}</div>
                                                """
            st.markdown(TractionRatioDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D2'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D3'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D4'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D5'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D6'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D7'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D8'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D9'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D10'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D11'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D12'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D13'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            GearboxEfficiencyQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D14'].value}</div>
            """
            st.markdown(GearboxEfficiencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            TractionRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D16'].value}</div>
            """
            st.markdown(TractionRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            TractionRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D17'].value}</div>
            """
            st.markdown(TractionRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            TractionRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D18'].value}</div>
            """
            st.markdown(TractionRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            TractionRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D19'].value}</div>
            """
            st.markdown(TractionRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            TractionRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D20'].value}</div>
            """
            st.markdown(TractionRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            TractionRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D21'].value}</div>
            """
            st.markdown(TractionRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            TractionRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D22'].value}</div>
            """
            st.markdown(TractionRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            TractionRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D23'].value}</div>
            """
            st.markdown(TractionRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            TractionRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D24'].value}</div>
            """
            st.markdown(TractionRatioQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            TractionRatioQuantity = f"""
            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D25'].value}</div>
            """
            st.markdown(TractionRatioQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            RopeQtyDescription = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E1'].value}</div>
                                        """
            st.markdown(RopeQtyDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            RatedSpeedDescription = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E15'].value}</div>
                                                    """
            st.markdown(RatedSpeedDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            RopeQtyQuantity = f"""
                <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E2'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E3'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E4'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E5'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E6'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E7'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E8'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E9'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E10'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E11'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E12'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E13'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            RopeQtyQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E14'].value}</div>
                """
            st.markdown(RopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            RatedSpeedQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E16'].value}</div>
                """
            st.markdown(RatedSpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            RatedSpeedQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E17'].value}</div>
                """
            st.markdown(RatedSpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            RatedSpeedQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E18'].value}</div>
                """
            st.markdown(RatedSpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            RatedSpeedQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E19'].value}</div>
                """
            st.markdown(RatedSpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            RatedSpeedQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E20'].value}</div>
                """
            st.markdown(RatedSpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            RatedSpeedQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E21'].value}</div>
                """
            st.markdown(RatedSpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            RatedSpeedQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E22'].value}</div>
                """
            st.markdown(RatedSpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            RatedSpeedQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E23'].value}</div>
                """
            st.markdown(RatedSpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            RatedSpeedQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E24'].value}</div>
                """
            st.markdown(RatedSpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            RatedSpeedQuantity = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E25'].value}</div>
                """
            st.markdown(RatedSpeedQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            RopeDiaDescription = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F1'].value}</div>
                                            """
            st.markdown(RopeDiaDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            BrakeVoltageDescription = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F15'].value}</div>
                                                        """
            st.markdown(BrakeVoltageDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            RopeDiaQuantity = f"""
                    <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F2'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F3'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F4'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F5'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F6'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F7'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F8'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F9'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F10'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F11'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F12'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F13'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            RopeDiaQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F14'].value}</div>
                    """
            st.markdown(RopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            BrakeVoltageQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F16'].value}</div>
                    """
            st.markdown(BrakeVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            BrakeVoltageQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F17'].value}</div>
                    """
            st.markdown(BrakeVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            BrakeVoltageQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F18'].value}</div>
                    """
            st.markdown(BrakeVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            BrakeVoltageQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F19'].value}</div>
                    """
            st.markdown(BrakeVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            BrakeVoltageQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F20'].value}</div>
                    """
            st.markdown(BrakeVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            BrakeVoltageQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F21'].value}</div>
                    """
            st.markdown(BrakeVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            BrakeVoltageQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F22'].value}</div>
                    """
            st.markdown(BrakeVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            BrakeVoltageQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F23'].value}</div>
                    """
            st.markdown(BrakeVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            BrakeVoltageQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F24'].value}</div>
                    """
            st.markdown(BrakeVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            BrakeVoltageQuantity = f"""
                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F25'].value}</div>
                    """
            st.markdown(BrakeVoltageQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            GrooveAngleDescription = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G1'].value}</div>
                                                """
            st.markdown(GrooveAngleDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            BrakeTorqueDescription = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G15'].value}</div>
                                                            """
            st.markdown(BrakeTorqueDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            GrooveAngleQuantity = f"""
                        <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G2'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G3'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G4'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G5'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G6'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G7'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G8'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G9'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G10'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G11'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G12'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G13'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            GrooveAngleQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G14'].value}</div>
                        """
            st.markdown(GrooveAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            BrakeTorqueQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G16'].value}</div>
                        """
            st.markdown(BrakeTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            BrakeTorqueQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G17'].value}</div>
                        """
            st.markdown(BrakeTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            BrakeTorqueQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G18'].value}</div>
                        """
            st.markdown(BrakeTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            BrakeTorqueQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G19'].value}</div>
                        """
            st.markdown(BrakeTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            BrakeTorqueQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G20'].value}</div>
                        """
            st.markdown(BrakeTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            BrakeTorqueQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G21'].value}</div>
                        """
            st.markdown(BrakeTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            BrakeTorqueQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G22'].value}</div>
                        """
            st.markdown(BrakeTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            BrakeTorqueQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G23'].value}</div>
                        """
            st.markdown(BrakeTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            BrakeTorqueQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G24'].value}</div>
                        """
            st.markdown(BrakeTorqueQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            BrakeTorqueQuantity = f"""
                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G25'].value}</div>
                        """
            st.markdown(BrakeTorqueQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            UndercutAngleDescription = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H1'].value}</div>
                                                    """
            st.markdown(UndercutAngleDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            VoltageDescription = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H15'].value}</div>
                                                                """
            st.markdown(VoltageDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            UndercutAngleQuantity = f"""
                            <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H2'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H3'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H4'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H5'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H6'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H7'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H8'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H9'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H10'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H11'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H12'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H13'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            UndercutAngleQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H14'].value}</div>
                            """
            st.markdown(UndercutAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            VoltageQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H16'].value}</div>
                            """
            st.markdown(VoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            VoltageQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H17'].value}</div>
                            """
            st.markdown(VoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            VoltageQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H18'].value}</div>
                            """
            st.markdown(VoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            VoltageQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H19'].value}</div>
                            """
            st.markdown(VoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            VoltageQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H20'].value}</div>
                            """
            st.markdown(VoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            VoltageQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H21'].value}</div>
                            """
            st.markdown(VoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            VoltageQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H22'].value}</div>
                            """
            st.markdown(VoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            VoltageQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H23'].value}</div>
                            """
            st.markdown(VoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            VoltageQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H24'].value}</div>
                            """
            st.markdown(VoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            VoltageQuantity = f"""
                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H25'].value}</div>
                            """
            st.markdown(VoltageQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            PitchDescription = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I1'].value}</div>
                                                        """
            st.markdown(PitchDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            CurrentDescription = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I15'].value}</div>
                                                                    """
            st.markdown(CurrentDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            PitchQuantity = f"""
                                <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I2'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I3'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I4'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I5'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I6'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I7'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I8'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I9'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I10'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I11'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I12'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I13'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            PitchQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I14'].value}</div>
                                """
            st.markdown(PitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            CurrentQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I16'].value}</div>
                                """
            st.markdown(CurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            CurrentQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I17'].value}</div>
                                """
            st.markdown(CurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            CurrentQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I18'].value}</div>
                                """
            st.markdown(CurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            CurrentQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I19'].value}</div>
                                """
            st.markdown(CurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            CurrentQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I20'].value}</div>
                                """
            st.markdown(CurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            CurrentQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I21'].value}</div>
                                """
            st.markdown(CurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            CurrentQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I22'].value}</div>
                                """
            st.markdown(CurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            CurrentQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I23'].value}</div>
                                """
            st.markdown(CurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            CurrentQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I24'].value}</div>
                                """
            st.markdown(CurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            CurrentQuantity = f"""
                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I25'].value}</div>
                                """
            st.markdown(CurrentQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            TractionSheaveDiaDescription = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J1'].value}</div>
                                                            """
            st.markdown(TractionSheaveDiaDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            PolesQtyDescription = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J15'].value}</div>
                                                                        """
            st.markdown(PolesQtyDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J2'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J3'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J4'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J5'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J6'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J7'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J8'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J9'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J10'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J11'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J12'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J13'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            TractionSheaveDiaQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J14'].value}</div>
                                    """
            st.markdown(TractionSheaveDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            PolesQtyQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J16'].value}</div>
                                    """
            st.markdown(PolesQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            PolesQtyQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J17'].value}</div>
                                    """
            st.markdown(PolesQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            PolesQtyQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J18'].value}</div>
                                    """
            st.markdown(PolesQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            PolesQtyQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J19'].value}</div>
                                    """
            st.markdown(PolesQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            PolesQtyQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J20'].value}</div>
                                    """
            st.markdown(PolesQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            PolesQtyQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J21'].value}</div>
                                    """
            st.markdown(PolesQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            PolesQtyQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J22'].value}</div>
                                    """
            st.markdown(PolesQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            PolesQtyQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J23'].value}</div>
                                    """
            st.markdown(PolesQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            PolesQtyQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J24'].value}</div>
                                    """
            st.markdown(PolesQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            PolesQtyQuantity = f"""
                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J25'].value}</div>
                                    """
            st.markdown(PolesQtyQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            WeightDescription = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K1'].value}</div>
                                                                """
            st.markdown(WeightDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            FrequencyDescription = f"""
                                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K15'].value}</div>
                                                                            """
            st.markdown(FrequencyDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            WeightQuantity = f"""
                                        <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K2'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K3'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K4'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K5'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K6'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K7'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K8'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K9'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K10'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K11'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K12'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K13'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            WeightQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K14'].value}</div>
                                        """
            st.markdown(WeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            FrequencyQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K16'].value}</div>
                                        """
            st.markdown(FrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            FrequencyQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K17'].value}</div>
                                        """
            st.markdown(FrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            FrequencyQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K18'].value}</div>
                                        """
            st.markdown(FrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            FrequencyQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K19'].value}</div>
                                        """
            st.markdown(FrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            FrequencyQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K20'].value}</div>
                                        """
            st.markdown(FrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            FrequencyQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K21'].value}</div>
                                        """
            st.markdown(FrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            FrequencyQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K22'].value}</div>
                                        """
            st.markdown(FrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            FrequencyQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K23'].value}</div>
                                        """
            st.markdown(FrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            FrequencyQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K24'].value}</div>
                                        """
            st.markdown(FrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            FrequencyQuantity = f"""
                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K25'].value}</div>
                                        """
            st.markdown(FrequencyQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            SpeedDescription = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L1'].value}</div>
                                                                    """
            st.markdown(SpeedDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            DiameterDescription = f"""
                                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L15'].value}</div>
                                                                                """
            st.markdown(DiameterDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            SpeedQuantity = f"""
                                            <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L2'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L3'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L4'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L5'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L6'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L7'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L8'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L9'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L10'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L11'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L12'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L13'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            SpeedQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L14'].value}</div>
                                            """
            st.markdown(SpeedQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            DiameterQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L16'].value}</div>
                                            """
            st.markdown(DiameterQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            DiameterQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L17'].value}</div>
                                            """
            st.markdown(DiameterQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            DiameterQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L18'].value}</div>
                                            """
            st.markdown(DiameterQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            DiameterQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L19'].value}</div>
                                            """
            st.markdown(DiameterQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            DiameterQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L20'].value}</div>
                                            """
            st.markdown(DiameterQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            DiameterQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L21'].value}</div>
                                            """
            st.markdown(DiameterQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            DiameterQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L22'].value}</div>
                                            """
            st.markdown(DiameterQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            DiameterQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L23'].value}</div>
                                            """
            st.markdown(DiameterQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            DiameterQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L24'].value}</div>
                                            """
            st.markdown(DiameterQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            DiameterQuantity = f"""
                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L25'].value}</div>
                                            """
            st.markdown(DiameterQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            NominalCurrentDescription = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M1'].value}</div>
                                                                        """
            st.markdown(NominalCurrentDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            SheaveRopeQtyDescription = f"""
                                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M15'].value}</div>
                                                                                    """
            st.markdown(SheaveRopeQtyDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M2'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M3'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M4'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M5'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M6'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M7'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M8'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M9'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M10'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M11'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M12'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M13'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            NominalCurrentQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M14'].value}</div>
                                                """
            st.markdown(NominalCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            SheaveRopeQtyQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M16'].value}</div>
                                                """
            st.markdown(SheaveRopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            SheaveRopeQtyQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M17'].value}</div>
                                                """
            st.markdown(SheaveRopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            SheaveRopeQtyQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M18'].value}</div>
                                                """
            st.markdown(SheaveRopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            SheaveRopeQtyQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M19'].value}</div>
                                                """
            st.markdown(SheaveRopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            SheaveRopeQtyQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M20'].value}</div>
                                                """
            st.markdown(SheaveRopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            SheaveRopeQtyQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M21'].value}</div>
                                                """
            st.markdown(SheaveRopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            SheaveRopeQtyQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M22'].value}</div>
                                                """
            st.markdown(SheaveRopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            SheaveRopeQtyQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M23'].value}</div>
                                                """
            st.markdown(SheaveRopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            SheaveRopeQtyQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M24'].value}</div>
                                                """
            st.markdown(SheaveRopeQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            SheaveRopeQtyQuantity = f"""
                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M25'].value}</div>
                                                """
            st.markdown(SheaveRopeQtyQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            StartCurrentDescription = f"""
                                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N1'].value}</div>
                                                                            """
            st.markdown(StartCurrentDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            SheaveRopeDiaDescription = f"""
                                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N15'].value}</div>
                                                                                        """
            st.markdown(SheaveRopeDiaDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N2'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N3'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N4'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N5'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N6'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N7'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N8'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N9'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N10'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N11'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N12'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N13'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            StartCurrentQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N14'].value}</div>
                                                    """
            st.markdown(StartCurrentQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            SheaveRopeDiaQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N16'].value}</div>
                                                    """
            st.markdown(SheaveRopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            SheaveRopeDiaQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N17'].value}</div>
                                                    """
            st.markdown(SheaveRopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            SheaveRopeDiaQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N18'].value}</div>
                                                    """
            st.markdown(SheaveRopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            SheaveRopeDiaQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N19'].value}</div>
                                                    """
            st.markdown(SheaveRopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            SheaveRopeDiaQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N20'].value}</div>
                                                    """
            st.markdown(SheaveRopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            SheaveRopeDiaQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N21'].value}</div>
                                                    """
            st.markdown(SheaveRopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            SheaveRopeDiaQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N22'].value}</div>
                                                    """
            st.markdown(SheaveRopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            SheaveRopeDiaQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N23'].value}</div>
                                                    """
            st.markdown(SheaveRopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            SheaveRopeDiaQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N24'].value}</div>
                                                    """
            st.markdown(SheaveRopeDiaQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            SheaveRopeDiaQuantity = f"""
                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N25'].value}</div>
                                                    """
            st.markdown(SheaveRopeDiaQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            CosPhiDescription = f"""
                                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O1'].value}</div>
                                                                                """
            st.markdown(CosPhiDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            BetaAngleDescription = f"""
                                                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O15'].value}</div>
                                                                                            """
            st.markdown(BetaAngleDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            CosPhiQuantity = f"""
                                                        <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O2'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O3'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O4'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O5'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O6'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O7'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O8'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O9'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O10'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O11'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O12'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O13'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            CosPhiQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O14'].value}</div>
                                                        """
            st.markdown(CosPhiQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            BetaAngleQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O16'].value}</div>
                                                        """
            st.markdown(BetaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            BetaAngleQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O17'].value}</div>
                                                        """
            st.markdown(BetaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            BetaAngleQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O18'].value}</div>
                                                        """
            st.markdown(BetaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            BetaAngleQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O19'].value}</div>
                                                        """
            st.markdown(BetaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            BetaAngleQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O20'].value}</div>
                                                        """
            st.markdown(BetaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            BetaAngleQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O21'].value}</div>
                                                        """
            st.markdown(BetaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            BetaAngleQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O22'].value}</div>
                                                        """
            st.markdown(BetaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            BetaAngleQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O23'].value}</div>
                                                        """
            st.markdown(BetaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            BetaAngleQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O24'].value}</div>
                                                        """
            st.markdown(BetaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            BetaAngleQuantity = f"""
                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O25'].value}</div>
                                                        """
            st.markdown(BetaAngleQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            MotorFrequencyDescription = f"""
                                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P1'].value}</div>
                                                                                    """
            st.markdown(MotorFrequencyDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            GamaAngleDescription = f"""
                                                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P15'].value}</div>
                                                                                                """
            st.markdown(GamaAngleDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P2'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P3'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P4'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P5'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P6'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P7'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P8'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P9'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P10'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P11'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P12'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P13'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            MotorFrequencyQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P14'].value}</div>
                                                            """
            st.markdown(MotorFrequencyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            GamaAngleQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P16'].value}</div>
                                                            """
            st.markdown(GamaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            GamaAngleQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P17'].value}</div>
                                                            """
            st.markdown(GamaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            GamaAngleQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P18'].value}</div>
                                                            """
            st.markdown(GamaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            GamaAngleQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P19'].value}</div>
                                                            """
            st.markdown(GamaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            GamaAngleQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P20'].value}</div>
                                                            """
            st.markdown(GamaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            GamaAngleQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P21'].value}</div>
                                                            """
            st.markdown(GamaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            GamaAngleQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P22'].value}</div>
                                                            """
            st.markdown(GamaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            GamaAngleQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P23'].value}</div>
                                                            """
            st.markdown(GamaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            GamaAngleQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P24'].value}</div>
                                                            """
            st.markdown(GamaAngleQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            GamaAngleQuantity = f"""
                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P25'].value}</div>
                                                            """
            st.markdown(GamaAngleQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            MotorVoltageDescription = f"""
                                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q1'].value}</div>
                                                                                        """
            st.markdown(MotorVoltageDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            GroovePitchDescription = f"""
                                                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q15'].value}</div>
                                                                                                    """
            st.markdown(GroovePitchDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q2'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q3'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q4'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q5'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q6'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q7'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q8'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q9'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q10'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q11'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q12'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q13'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            MotorVoltageQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q14'].value}</div>
                                                                """
            st.markdown(MotorVoltageQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            GroovePitchQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q16'].value}</div>
                                                                """
            st.markdown(GroovePitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            GroovePitchQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q17'].value}</div>
                                                                """
            st.markdown(GroovePitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            GroovePitchQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q18'].value}</div>
                                                                """
            st.markdown(GroovePitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            GroovePitchQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q19'].value}</div>
                                                                """
            st.markdown(GroovePitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            GroovePitchQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q20'].value}</div>
                                                                """
            st.markdown(GroovePitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            GroovePitchQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q21'].value}</div>
                                                                """
            st.markdown(GroovePitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            GroovePitchQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q22'].value}</div>
                                                                """
            st.markdown(GroovePitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            GroovePitchQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q23'].value}</div>
                                                                """
            st.markdown(GroovePitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            GroovePitchQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q24'].value}</div>
                                                                """
            st.markdown(GroovePitchQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            GroovePitchQuantity = f"""
                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q25'].value}</div>
                                                                """
            st.markdown(GroovePitchQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            PoleQtyDescription = f"""
                                                                                            <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R1'].value}</div>
                                                                                            """
            st.markdown(PoleQtyDescription, unsafe_allow_html=True)
        elif ws1['B2'].value == ws1['D2'].value:
            MotorWeightDescription = f"""
                                                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R15'].value}</div>
                                                                                                        """
            st.markdown(MotorWeightDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R2'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R3'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R4'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R5'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R6'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R7'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R8'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R9'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R10'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R11'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R12'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R13'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            PoleQtyQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R14'].value}</div>
                                                                    """
            st.markdown(PoleQtyQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A16'].value:
            MotorWeightQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R16'].value}</div>
                                                                    """
            st.markdown(MotorWeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A17'].value:
            MotorWeightQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R17'].value}</div>
                                                                    """
            st.markdown(MotorWeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A18'].value:
            MotorWeightQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R18'].value}</div>
                                                                    """
            st.markdown(MotorWeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A19'].value:
            MotorWeightQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R19'].value}</div>
                                                                    """
            st.markdown(MotorWeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A20'].value:
            MotorWeightQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R20'].value}</div>
                                                                    """
            st.markdown(MotorWeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A21'].value:
            MotorWeightQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R21'].value}</div>
                                                                    """
            st.markdown(MotorWeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A22'].value:
            MotorWeightQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R22'].value}</div>
                                                                    """
            st.markdown(MotorWeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A23'].value:
            MotorWeightQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R23'].value}</div>
                                                                    """
            st.markdown(MotorWeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A24'].value:
            MotorWeightQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R24'].value}</div>
                                                                    """
            st.markdown(MotorWeightQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A25'].value:
            MotorWeightQuantity = f"""
                                                                    <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R25'].value}</div>
                                                                    """
            st.markdown(MotorWeightQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B2'].value == ws1['C2'].value:
            EdDescription = f"""
                                                                                                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S1'].value}</div>
                                                                                                """
            st.markdown(EdDescription, unsafe_allow_html=True)
    with cols[1]:
        if ws2['A1'].value == ws2['A2'].value:
            EdQuantity = f"""
                                                                        <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S2'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A3'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S3'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A4'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S4'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A5'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S5'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A6'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S6'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A7'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S7'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A8'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S8'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A9'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S9'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A10'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S10'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A11'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S11'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A12'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S12'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A13'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S13'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)
        elif ws2['A1'].value == ws2['A14'].value:
            EdQuantity = f"""
                                                                        <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S14'].value}</div>
                                                                        """
            st.markdown(EdQuantity, unsafe_allow_html=True)




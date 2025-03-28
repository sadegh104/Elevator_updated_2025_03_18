import math
import streamlit as st
from openpyxl import load_workbook
st.set_page_config("Elevator Calculator", layout="wide")
wb = load_workbook('Data-Ranjbar.xlsx')
with st.sidebar:
    st.title("تحلیل محاسبات آسانسور")
cols = st.columns(3)
with cols[0]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb18 = ws['B18']
            cellc18 = ws['C18']
            celld18 = ws['D18']
            new_valueb18 = st.selectbox('نوع موتورخانه', options=[cellc18.value, celld18.value],
                                       key=f'{cellb18.coordinate}_{sheet_name}')
            if new_valueb18 == cellc18.value:
                cellb18.value = cellc18.value
            elif new_valueb18 == celld18.value:
                cellb18.value = celld18.value

with cols[1]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb18 = ws['B18']
            cellc18 = ws['C18']
            celld18 = ws['D18']
            cellb19 = ws['B19']
            cellc19 = ws['C19']
            celld19 = ws['D19']
            if cellb18.value == cellc18.value:
                new_valueb19 = st.selectbox('نوع موتور', options=[cellc19.value, celld19.value],
                                            key=f'{cellb19.coordinate}_{sheet_name}')
                if new_valueb19 == cellc19.value:
                    cellb19.value = cellc19.value
                elif new_valueb19 == celld19.value:
                    cellb19.value = celld19.value
            elif cellb18.value == celld18.value:
                new_valueb19 = st.selectbox('نوع موتور', options=[celld19.value],
                                            key=f'{cellb19.coordinate}_{sheet_name}')
                if new_valueb19 == celld19.value:
                    cellb19.value = celld19.value
with cols[2]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb19 = ws['B19']
            cellc19 = ws['C19']
            celld19 = ws['D19']
            cellb20 = ws['B20']
            cellc20 = ws['C20']
            celld20 = ws['D20']
            celle20 = ws['E20']
            if cellb19.value == cellc19.value:
                new_valueb20 = st.selectbox('سیستم تعلیق', options=[cellc20.value],
                                            key=f'{cellb20.coordinate}_{sheet_name}')
                if new_valueb20 == cellc20.value:
                    cellb20.value = cellc20.value
            elif cellb19.value == celld19.value:
                new_valueb20 = st.selectbox('سیستم تعلیق', options=[cellc20.value, celld20.value, celle20.value],
                                            key=f'{cellb20.coordinate}_{sheet_name}')
                if new_valueb20 == cellc20.value:
                    cellb20.value = cellc20.value
                elif new_valueb20 == celld20.value:
                    cellb20.value = celld20.value
                elif new_valueb20 == celle20.value:
                    cellb20.value = celle20.value
cols = st.columns(3)
with cols[0]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb2 = ws['B2']
            new_valueb2 = st.number_input('تعداد آسانسور',
                                          key=f'{cellb2.coordinate}_{sheet_name}', value=1)

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
            cellj3 = ws['J3']
            cellk3 = ws['K3']
            celll3 = ws['L3']
            new_valueb3 = st.selectbox('ظرفیت (نفر)', options=[cellc3.value, celld3.value, celle3.value, cellf3.value, cellg3.value, cellh3.value, celli3.value, cellj3.value, cellk3.value, celll3.value],
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
            elif new_valueb3 == cellj3.value:
                cellb3.value = cellj3.value
            elif new_valueb3 == cellk3.value:
                cellb3.value = cellk3.value
            elif new_valueb3 == celll3.value:
                cellb3.value = celll3.value
with cols[2]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            # cellb3 = ws['B3']
            # cellc3 = ws['C3']
            # celld3 = ws['D3']
            # celle3 = ws['E3']
            # cellf3 = ws['F3']
            # cellg3 = ws['G3']
            # cellh3 = ws['H3']
            # celli3 = ws['I3']
            # cellj3 = ws['J3']
            # cellk3 = ws['K3']
            # celll3 = ws['L3']
            cellb4 = ws['B4']
            cellc4 = ws['C4']
            celld4 = ws['D4']
            cellb18 = ws['B18']
            cellc18 = ws['C18']
            celld18 = ws['D18']
            if cellb18.value == cellc18.value:
                new_valueb4 = st.selectbox('نوع آسانسور', options=[celld4.value],
                                           key=f'{cellb4.coordinate}_{sheet_name}')
                if new_valueb4 == celld4.value:
                    cellb4.value = celld4.value
            elif cellb18.value == celld18.value:
                new_valueb4 = st.selectbox('نوع آسانسور', options=[cellc4.value],
                                           key=f'{cellb4.coordinate}_{sheet_name}')
                if new_valueb4 == cellc4.value:
                    cellb4.value = cellc4.value
            # if cellb3.value == cellc3.value:
            #     new_valueb4 = st.selectbox('نوع آسانسور', options=[cellc4.value],
            #                                key=f'{cellb4.coordinate}_{sheet_name}')
            #     if new_valueb4 == cellc4.value:
            #         cellb4.value = cellc4.value
            # elif cellb3.value == celld3.value:
            #     new_valueb4 = st.selectbox('نوع آسانسور', options=[cellc4.value, celld4.value],
            #                                key=f'{cellb4.coordinate}_{sheet_name}')
            #     if new_valueb4 == cellc4.value:
            #         cellb4.value = cellc4.value
            #     elif new_valueb4 == celld4.value:
            #         cellb4.value = celld4.value
            # elif cellb3.value == celle3.value or cellb3.value == cellf3.value:
            #     new_valueb4 = st.selectbox('نوع آسانسور', options=[celld4.value],
            #                                key=f'{cellb4.coordinate}_{sheet_name}')
            #     if new_valueb4 == celld4.value:
            #         cellb4.value = celld4.value
            # new_valueb4 = st.selectbox('نوع آسانسور', options=[celld4.value],
            #                             key=f'{cellb4.coordinate}_{sheet_name}')
            # if new_valueb4 == celld4.value:
            #     cellb4.value = celld4.value
cols = st.columns(3)
with cols[0]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb10 = ws['B10']
            new_valueb10 = st.number_input('(متر) چاهک',
                                           key=f'{cellb10.coordinate}_{sheet_name}', value=1.5)
with cols[1]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb6 = ws['B6']
            cellc6 = ws['C6']
            celld6 = ws['D6']
            celle6 = ws['E6']
            cellf6 = ws['F6']
            cellg6 = ws['G6']
            cellh6 = ws['H6']
            celli6 = ws['I6']
            new_valueb6 = st.selectbox('تعداد توقف',
                                       options=[cellc6.value, celld6.value, celle6.value, cellf6.value, cellg6.value,
                                                cellh6.value, celli6.value],
                                       key=f'{cellb6.coordinate}_{sheet_name}')
            if new_valueb6 == cellc6.value:
                cellb6.value = cellc6.value
            elif new_valueb6 == celld6.value:
                cellb6.value = celld6.value
            elif new_valueb6 == celle6.value:
                cellb6.value = celle6.value
            elif new_valueb6 == cellf6.value:
                cellb6.value = cellf6.value
            elif new_valueb6 == cellg6.value:
                cellb6.value = cellg6.value
            elif new_valueb6 == cellh6.value:
                cellb6.value = cellh6.value
            elif new_valueb6 == celli6.value:
                cellb6.value = celli6.value
with cols[2]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb14 = ws['B14']
            cellc14 = ws['C14']
            celld14 = ws['D14']
            celle14 = ws['E14']
            new_valueb14 = st.selectbox('عرض وزنه تعادل', options=[cellc14.value, celld14.value, celle14.value],
                                        key=f'{cellb14.coordinate}_{sheet_name}')
            if new_valueb14 == cellc14.value:
                cellb14.value = cellc14.value
            elif new_valueb14 == celld14.value:
                cellb14.value = celld14.value
            elif new_valueb14 == celle14.value:
                cellb14.value = celle14.value

cols = st.columns(3)
with cols[0]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb9 = ws['B9']
            new_valueb9 = st.number_input('(متر) اورهد',
                                          key=f'{cellb9.coordinate}_{sheet_name}', value=3.9)
with cols[1]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb11 = ws['B11']
            cellc11 = ws['C11']
            celld11 = ws['D11']
            new_valueb11 = st.selectbox('نوع درب', options=[cellc11.value, celld11.value],
                                        key=f'{cellb11.coordinate}_{sheet_name}')
            if new_valueb11 == cellc11.value:
                cellb11.value = cellc11.value
            elif new_valueb11 == celld11.value:
                cellb11.value = celld11.value
with cols[2]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb11 = ws['B11']
            cellc11 = ws['C11']
            celld11 = ws['D11']
            cellb13 = ws['B13']
            cellc13 = ws['C13']
            celld13 = ws['D13']
            celle13 = ws['E13']
            if cellb11.value == cellc11.value:
                new_valueb13 = st.selectbox('جهت درب', options=[cellc13.value, celld13.value, celle13.value],
                                            key=f'{cellb13.coordinate}_{sheet_name}')
                if new_valueb13 == cellc13.value:
                    cellb13.value = cellc13.value
                elif new_valueb13 == celld13.value:
                    cellb13.value = celld13.value
                elif new_valueb13 == celle13.value:
                    cellb13.value = celle13.value
            elif cellb11.value == celld11.value:
                new_valueb13 = st.selectbox('جهت درب', options=[cellc13.value, celld13.value],
                                            key=f'{cellb13.coordinate}_{sheet_name}')
                if new_valueb13 == cellc13.value:
                    cellb13.value = cellc13.value
                elif new_valueb13 == celld13.value:
                    cellb13.value = celld13.value

cols = st.columns(3)
with cols[0]:
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
            cellj3 = ws['J3']
            cellk3 = ws['K3']
            celll3 = ws['L3']
            cellb16 = ws['B16']
            if cellb3.value == cellc3.value: 
                new_valueb16 = st.number_input('وزن کابین (کیلوگرم)',
                                          key=f'{cellb16.coordinate}_{sheet_name}', value=400)
            elif cellb3.value == celld3.value: 
                new_valueb16 = st.number_input('وزن کابین (کیلوگرم)',
                                          key=f'{cellb16.coordinate}_{sheet_name}', value=450)
            elif cellb3.value == celle3.value: 
                new_valueb16 = st.number_input('وزن کابین (کیلوگرم)',
                                          key=f'{cellb16.coordinate}_{sheet_name}', value=500)
            elif cellb3.value == cellf3.value: 
                new_valueb16 = st.number_input('وزن کابین (کیلوگرم)',
                                          key=f'{cellb16.coordinate}_{sheet_name}', value=550)
            elif cellb3.value == cellg3.value: 
                new_valueb16 = st.number_input('وزن کابین (کیلوگرم)',
                                          key=f'{cellb16.coordinate}_{sheet_name}', value=600)
            elif cellb3.value == cellh3.value: 
                new_valueb16 = st.number_input('وزن کابین (کیلوگرم)',
                                          key=f'{cellb16.coordinate}_{sheet_name}', value=675)
            elif cellb3.value == celli3.value: 
                new_valueb16 = st.number_input('وزن کابین (کیلوگرم)',
                                          key=f'{cellb16.coordinate}_{sheet_name}', value=750)
            elif cellb3.value == cellj3.value: 
                new_valueb16 = st.number_input('وزن کابین (کیلوگرم)',
                                          key=f'{cellb16.coordinate}_{sheet_name}', value=800)
            elif cellb3.value == cellk3.value: 
                new_valueb16 = st.number_input('وزن کابین (کیلوگرم)',
                                          key=f'{cellb16.coordinate}_{sheet_name}', value=850)
            elif cellb3.value == celll3.value: 
                new_valueb16 = st.number_input('وزن کابین (کیلوگرم)',
                                          key=f'{cellb16.coordinate}_{sheet_name}', value=900)
with cols[1]:
    cellb11 = ws['B11']
    cellc11 = ws['C11']
    celld11 = ws['D11']
    cellb12 = ws['B12']
    cellc12 = ws['C12']
    celld12 = ws['D12']
    celle12 = ws['E12']
    cellf12 = ws['F12']
    if cellb11.value == cellc11.value:
        new_valueb12 = st.selectbox('عرض درب',
                                    options=[cellc12.value, celld12.value, celle12.value, cellf12.value],
                                    key=f'{cellb12.coordinate}_{sheet_name}')
        if new_valueb12 == cellc12.value:
            cellb12.value = cellc12.value
        elif new_valueb12 == celld12.value:
            cellb12.value = celld12.value
        elif new_valueb12 == celle12.value:
            cellb12.value = celle12.value
        elif new_valueb12 == cellf12.value:
            cellb12.value = cellf12.value
    elif cellb11.value == celld11.value:
        new_valueb12 = st.selectbox('عرض درب', options=[cellc12.value, celld12.value, celle12.value],
                                    key=f'{cellb12.coordinate}_{sheet_name}')
        if new_valueb12 == cellc12.value:
            cellb12.value = cellc12.value
        elif new_valueb12 == celld12.value:
            cellb12.value = celld12.value
        elif new_valueb12 == celle12.value:
            cellb12.value = celle12.value
with cols[2]:
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
            cellj3 = ws['J3']
            cellk3 = ws['K3']
            celll3 = ws['L3']
            cellb17 = ws['B17']
            if cellb3.value == cellc3.value: 
                new_valueb17 = st.number_input('تعداد شیار فلکه موتور',
                                          key=f'{cellb17.coordinate}_{sheet_name}', value=5)
            elif cellb3.value == celld3.value: 
                new_valueb17 = st.number_input('تعداد شیار فلکه موتور',
                                          key=f'{cellb17.coordinate}_{sheet_name}', value=5)
            elif cellb3.value == celle3.value: 
                new_valueb17 = st.number_input('تعداد شیار فلکه موتور',
                                          key=f'{cellb17.coordinate}_{sheet_name}', value=5)
            elif cellb3.value == cellf3.value: 
                new_valueb17 = st.number_input('تعداد شیار فلکه موتور',
                                          key=f'{cellb17.coordinate}_{sheet_name}', value=5)
            elif cellb3.value == cellg3.value: 
                new_valueb17 = st.number_input('تعداد شیار فلکه موتور',
                                          key=f'{cellb17.coordinate}_{sheet_name}', value=5)
            elif cellb3.value == cellh3.value: 
                new_valueb17 = st.number_input('تعداد شیار فلکه موتور',
                                          key=f'{cellb17.coordinate}_{sheet_name}', value=6)
            elif cellb3.value == celli3.value: 
                new_valueb17 = st.number_input('تعداد شیار فلکه موتور',
                                          key=f'{cellb17.coordinate}_{sheet_name}', value=6)
            elif cellb3.value == cellj3.value: 
                new_valueb17 = st.number_input('تعداد شیار فلکه موتور',
                                          key=f'{cellb17.coordinate}_{sheet_name}', value=6)
            elif cellb3.value == cellk3.value: 
                new_valueb17 = st.number_input('تعداد شیار فلکه موتور',
                                          key=f'{cellb17.coordinate}_{sheet_name}', value=6)
            elif cellb3.value == celll3.value: 
                new_valueb17 = st.number_input('تعداد شیار فلکه موتور',
                                          key=f'{cellb17.coordinate}_{sheet_name}', value=6)
cols = st.columns(3)
with cols[2]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb20 = ws['B20']
            cellc20 = ws['C20']
            celld20 = ws['D20']
            celle20 = ws['E20']
            cellb21 = ws['B21']
            if cellb20.value == cellc20.value:
                new_valueb21 = st.number_input('فاصله فلکه های کابین (متر)',
                                           key=f'{cellb21.coordinate}_{sheet_name}', value=0.75)
            elif cellb20.value == celld20.value or cellb20.value == celle20.value:
                new_valueb21 = st.number_input('فاصله فلکه های کابین (متر)',
                                           key=f'{cellb21.coordinate}_{sheet_name}', value=0.50)
            
with cols[1]:
    sheet_names = wb.sheetnames
    for sheet_name in sheet_names:
        if sheet_name == 'Data (1)':
            ws = wb[sheet_name]
            cellb5 = ws['B5']
            cellc5 = ws['C5']
            celld5 = ws['D5']
            new_valueb5 = st.selectbox('سرعت آسانسور',
                                       options=[cellc5.value, celld5.value],
                                       key=f'{cellb5.coordinate}_{sheet_name}')
            if new_valueb5 == cellc5.value:
                cellb5.value = cellc5.value
            elif new_valueb5 == celld5.value:
                cellb5.value = celld5.value



if st.button('ثبت'):
    ws1 = wb['Data (1)']
    ws2 = wb['Data (2)']
    new_valueb3 = ws1['B3'].value
    new_valuec3 = ws1['C3'].value
    new_valued3 = ws1['D3'].value
    new_valuee3 = ws1['E3'].value
    new_valuef3 = ws1['F3'].value
    new_valueg3 = ws1['G3'].value
    new_valueh3 = ws1['H3'].value
    new_valuei3 = ws1['I3'].value
    new_valuej3 = ws1['J3'].value
    new_valuek3 = ws1['K3'].value
    new_valuel3 = ws1['L3'].value
    new_valueb5 = ws1['B5'].value
    new_valuec5 = ws1['C5'].value
    new_valued5 = ws1['D5'].value
    new_valueb8 = (new_valueb6 - 1) * 3.4
    new_valueb11 = ws1['B11'].value
    new_valuec11 = ws1['C11'].value
    new_valued11 = ws1['D11'].value
    new_valueb12 = ws1['B12'].value
    new_valuec12 = ws1['C12'].value
    new_valued12 = ws1['D12'].value
    new_valuee12 = ws1['E12'].value
    new_valuef12 = ws1['F12'].value
    new_valueb13 = ws1['B13'].value
    new_valuec13 = ws1['C13'].value
    new_valued13 = ws1['D13'].value
    new_valuee13 = ws1['E13'].value
    new_valueb6 = ws1['B6'].value
    new_valuec6 = ws1['C6'].value
    new_valued6 = ws1['D6'].value
    new_valuee6 = ws1['E6'].value
    new_valuef6 = ws1['F6'].value
    new_valueg6 = ws1['G6'].value
    new_valueh6 = ws1['H6'].value
    new_valuei6 = ws1['I6'].value
    new_valueb14 = ws1['B14'].value
    new_valuec14 = ws1['C14'].value
    new_valued14 = ws1['D14'].value
    new_valuee14 = ws1['E14'].value
    new_valueb18 = ws1['B18'].value
    new_valuec18 = ws1['C18'].value
    new_valued18 = ws1['D18'].value
    new_valueb19 = ws1['B19'].value
    new_valuec19 = ws1['C19'].value
    new_valued19 = ws1['D19'].value
    new_valueb20 = ws1['B20'].value
    new_valuec20 = ws1['C20'].value
    new_valued20 = ws1['D20'].value
    new_valuee20 = ws1['E20'].value

    cols = st.columns(2)
    with cols[0]:
        EquipmentDescription = f"""
                        <div  style='padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>شرح متریال</div>
                        """
        st.markdown(EquipmentDescription, unsafe_allow_html=True)
    with cols[1]:
        QuantityDescription = f"""
                                <div  style='padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>تعداد</div>
                                """
        st.markdown(QuantityDescription, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B5'].value == ws1['C5'].value and ws1['B19'].value == ws1['C19'].value: 
            if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value:
                MotorDescription = f"""
                <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A2'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value) and (ws1['B4'].value == ws1['C4'].value):
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A3'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value) and (ws1['B4'].value == ws1['D4'].value):
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A4'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A5'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
        elif ws1['B5'].value == ws1['D5'].value and ws1['B19'].value == ws1['C19'].value:
            if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value:
                MotorDescription = f"""
                <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A6'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value) and (ws1['B4'].value == ws1['C4'].value):
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A7'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value) and (ws1['B4'].value == ws1['D4'].value):
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A8'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A9'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
        elif ws1['B5'].value == ws1['C5'].value and ws1['B19'].value == ws1['D19'].value:
            if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value:
                MotorDescription = f"""
                <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A10'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value) and (ws1['B4'].value == ws1['C4'].value):
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A11'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value) and (ws1['B4'].value == ws1['D4'].value):
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A12'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A13'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
        elif ws1['B5'].value == ws1['D5'].value and ws1['B19'].value == ws1['D19'].value:
            if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value:
                MotorDescription = f"""
                <div  style='display:flex;flex-wrap:wrap;background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A14'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value) and (ws1['B4'].value == ws1['C4'].value):
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A15'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value) and (ws1['B4'].value == ws1['D4'].value):
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A16'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
            elif ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
                MotorDescription = f"""
                <div  style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['A17'].value}</div>
                """
                st.markdown(MotorDescription, unsafe_allow_html=True)
    with cols[1]:
        MotorQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{int(new_valueb2)}</div>
                """
        st.markdown(MotorQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            RailT90Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B2'].value}</div>
                    """
            st.markdown(RailT90Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valuej3 or new_valueb3 == new_valuek3 or new_valueb3 == new_valuel3:
            if (((new_valueb8 + new_valueb9 + new_valueb10)*0.4) - int((new_valueb8 + new_valueb9 + new_valueb10)*0.4) > 0.1):
                RailT90Quantity = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*(int((new_valueb8 + new_valueb9 + new_valueb10)*0.4)+1)}</div>
                                    """
                st.markdown(RailT90Quantity, unsafe_allow_html=True)
            else:
                RailT90Quantity = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*(int((new_valueb8 + new_valueb9 + new_valueb10)*0.4))}</div>
                                    """
                st.markdown(RailT90Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            PoshtBandRailT90Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C2'].value}</div>
                    """
            st.markdown(PoshtBandRailT90Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valuej3 or new_valueb3 == new_valuek3 or new_valueb3 == new_valuel3:
            if (((new_valueb8 + new_valueb9 + new_valueb10)*0.4) - int((new_valueb8 + new_valueb9 + new_valueb10)*0.4) > 0.1):
                RailT90Quant = (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4) + 1)
                if (RailT90Quant / new_valueb2) % 2 == 0:
                    PoshtBandRailT90Quantity = f"""
                                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*int((RailT90Quant / new_valueb2) - 2)}</div>
                                                        """
                    st.markdown(PoshtBandRailT90Quantity, unsafe_allow_html=True)
                else:
                    PoshtBandRailT90Quantity = f"""
                                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*int((RailT90Quant / new_valueb2) - 1)}</div>
                                                        """
                    st.markdown(PoshtBandRailT90Quantity, unsafe_allow_html=True)
                # PoshtBandRailT90Quantity = f"""
                #                                     <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4) + 1)}</div>
                #                                     """
                # st.markdown(PoshtBandRailT90Quantity, unsafe_allow_html=True)
            else:
                RailT90Quant = (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4))
                if (RailT90Quant / new_valueb2) % 2 == 0:
                    PoshtBandRailT90Quantity = f"""
                                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*int((RailT90Quant / new_valueb2) - 2)}</div>
                                                            """
                    st.markdown(PoshtBandRailT90Quantity, unsafe_allow_html=True)
                else:
                    PoshtBandRailT90Quantity = f"""
                                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*((RailT90Quant / new_valueb2) - 1)}</div>
                                                            """
                    st.markdown(PoshtBandRailT90Quantity, unsafe_allow_html=True)
                # PoshtBandRailT90Quantity = f"""
                #                                     <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4))}</div>
                #                                     """
                # st.markdown(PoshtBandRailT90Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value != ws1['J3'].value and ws1['B3'].value != ws1['K3'].value and ws1['B3'].value != ws1['L3'].value:
            RailT70Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B3'].value}</div>
                    """
            st.markdown(RailT70Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 != new_valuej3 and new_valueb3 != new_valuek3 and new_valueb3 != new_valuel3:
            if (((new_valueb8 + new_valueb9 + new_valueb10)*0.4) - int((new_valueb8 + new_valueb9 + new_valueb10)*0.4) > 0.1):
                RailT70Quantity = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*(int((new_valueb8 + new_valueb9 + new_valueb10)*0.4)+1)}</div>
                                    """
                st.markdown(RailT70Quantity, unsafe_allow_html=True)
            else:
                RailT70Quantity = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*(int((new_valueb8 + new_valueb9 + new_valueb10)*0.4))}</div>
                                    """
                st.markdown(RailT70Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value != ws1['J3'].value and ws1['B3'].value != ws1['K3'].value and ws1['B3'].value != ws1['L3'].value:
            PoshtBandRailT70Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C3'].value}</div>
                    """
            st.markdown(PoshtBandRailT70Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 != new_valuej3 and new_valueb3 != new_valuek3 and new_valueb3 != new_valuel3:
            if (((new_valueb8 + new_valueb9 + new_valueb10)*0.4) - int((new_valueb8 + new_valueb9 + new_valueb10)*0.4) > 0.1):
                RailT70Quant = (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4) + 1)
                if (RailT70Quant / new_valueb2) % 2 == 0:
                    PoshtBandRailT70Quantity = f"""
                                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*int((RailT70Quant / new_valueb2) - 2)}</div>
                                                            """
                    st.markdown(PoshtBandRailT70Quantity, unsafe_allow_html=True)
                else:
                    PoshtBandRailT70Quantity = f"""
                                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*int((RailT70Quant / new_valueb2) - 1)}</div>
                                                            """
                    st.markdown(PoshtBandRailT70Quantity, unsafe_allow_html=True)
                # PoshtBandRailT70Quantity = f"""
                #                                     <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4) + 1)}</div>
                #                                     """
                # st.markdown(PoshtBandRailT70Quantity, unsafe_allow_html=True)
            else:
                RailT70Quant = (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4))
                if (RailT70Quant / new_valueb2) % 2 == 0:
                    PoshtBandRailT70Quantity = f"""
                                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*int((RailT70Quant / new_valueb2) - 2)}</div>
                                                            """
                    st.markdown(PoshtBandRailT70Quantity, unsafe_allow_html=True)
                else:
                    PoshtBandRailT70Quantity = f"""
                                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*int((RailT70Quant / new_valueb2) - 1)}</div>
                                                            """
                    st.markdown(PoshtBandRailT70Quantity, unsafe_allow_html=True)
                # PoshtBandRailT70Quantity = f"""
                #                                     <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4))}</div>
                #                                     """
                # st.markdown(PoshtBandRailT70Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        RailT50Description = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['B4'].value}</div>
                                    """
        st.markdown(RailT50Description, unsafe_allow_html=True)
    with cols[1]:
        RailT50Quantity = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4) + 1)}</div>
                                    """
        st.markdown(RailT50Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        PoshtBandRailT50Description = f"""
                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['C4'].value}</div>
                                            """
        st.markdown(PoshtBandRailT50Description, unsafe_allow_html=True)
    with cols[1]:
        RailT50Quant = (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4) + 1)
        if (RailT50Quant / new_valueb2) % 2 == 0:
            PoshtBandRailT50Quantity = f"""
                                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*int((RailT50Quant / new_valueb2) - 2)}</div>
                                                    """
            st.markdown(PoshtBandRailT50Quantity, unsafe_allow_html=True)
        else:
            PoshtBandRailT50Quantity = f"""
                                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*int((RailT50Quant / new_valueb2) - 1)}</div>
                                                    """
            st.markdown(PoshtBandRailT50Quantity, unsafe_allow_html=True)
        # PoshtBandRailT50Quantity = f"""
        #                                     <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * (int((new_valueb8 + new_valueb9 + new_valueb10) * 0.4) + 1)}</div>
        #                                     """
        # st.markdown(PoshtBandRailT50Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            LoghmeRailT90Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D2'].value}</div>
                    """
            st.markdown(LoghmeRailT90Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valuej3 or new_valueb3 == new_valuek3 or new_valueb3 == new_valuel3:
            LoghmeRailT90Quantity = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(math.ceil((new_valueb2) * ((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4)))*2}</div>
                    """
            st.markdown(LoghmeRailT90Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value != ws1['J3'].value and ws1['B3'].value != ws1['K3'].value and ws1['B3'].value != ws1['L3'].value:
            LoghmeRailT70Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D3'].value}</div>
                    """
            st.markdown(LoghmeRailT70Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 != new_valuej3 and new_valueb3 != new_valuek3 and new_valueb3 != new_valuel3:
            LoghmeRailT70Quantity = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(math.ceil((new_valueb2) * ((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4)))*2}</div>
                            """
            st.markdown(LoghmeRailT70Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        LoghmeRailT50Description = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['D4'].value}</div>
                                    """
        st.markdown(LoghmeRailT50Description, unsafe_allow_html=True)
    with cols[1]:
        LoghmeRailT50Quantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(math.ceil((new_valueb2) * ((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4))) * 2}</div>
                                """
        st.markdown(LoghmeRailT50Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        BracketCabinDescription = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['E2'].value}</div>
                                        """
        st.markdown(BracketCabinDescription, unsafe_allow_html=True)
    with cols[1]:
        BracketCabinQuantity = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(math.ceil((new_valueb2) * ((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4)))}</div>
                        """
        st.markdown(BracketCabinQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        LeftBracketWazneDescription = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F2'].value}</div>
                                        """
        st.markdown(LeftBracketWazneDescription, unsafe_allow_html=True)
    with cols[1]:
        LeftBracketWazneQuantity = f"""
                       <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(math.ceil((new_valueb2) * (((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) + 2)))}</div>
                       """
        st.markdown(LeftBracketWazneQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        RightBracketWazneDescription = f"""
                                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['F3'].value}</div>
                                                """
        st.markdown(RightBracketWazneDescription, unsafe_allow_html=True)
    with cols[1]:
        RightBracketWazneQuantity = f"""
                               <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(math.ceil((new_valueb2) * (((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) + 2)))}</div>
                               """
        st.markdown(RightBracketWazneQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        Pitch10Description = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G2'].value}</div>
                                        """
        st.markdown(Pitch10Description, unsafe_allow_html=True)
    with cols[1]:
        LeftBracketWazneQuant = math.ceil((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) + 2))
        # LoghmeRailT50Quant = int(math.ceil(((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4))) * 2
        # Pitch10Quantity = f"""
        #                 <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(2 * int(LeftBracketWazneQuant) + LoghmeRailT50Quant)}</div>
        #                 """
        # st.markdown(Pitch10Quantity, unsafe_allow_html=True)
        # LoghmeRailT50Quant = int(math.ceil(((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4))) * 2
        Pitch10Quantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(2 * int(LeftBracketWazneQuant))}</div>
                                """
        st.markdown(Pitch10Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value != ws1['J3'].value and ws1['B3'].value != ws1['K3'].value and ws1['B3'].value != ws1['L3'].value:
            Pitch12Description = f"""
                                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G3'].value}</div>
                                                    """
            st.markdown(Pitch12Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 != new_valuej3 and new_valueb3 != new_valuek3 and new_valueb3 != new_valuel3:
            BracketCabinQuant = int(math.ceil(((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4)))
            # LoghmeRailT70Quant = int(math.ceil(((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4))) * 2
            # Pitch12Quantity = f"""
            #                         <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(2 * int(BracketCabinQuant) + LoghmeRailT70Quant)}</div>
            #                         """
            # st.markdown(Pitch12Quantity, unsafe_allow_html=True)
            # LoghmeRailT70Quant = int(math.ceil(((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4))) * 2
            Pitch12Quantity = f"""
                                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(2 * int(BracketCabinQuant))}</div>
                                                """
            st.markdown(Pitch12Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        Pitch8Description = f"""
                                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['G4'].value}</div>
                                                """
        st.markdown(Pitch8Description, unsafe_allow_html=True)
    with cols[1]:
        LeftBracketWazneQuant = math.ceil((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) + 2))
        # LoghmeRailT50Quant = int(math.ceil(((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4))) * 2
        # Pitch8Quantity = f"""
        #                         <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(2 * int(LeftBracketWazneQuant) + LoghmeRailT50Quant)}</div>
        #                         """
        # st.markdown(Pitch8Quantity, unsafe_allow_html=True)
        # LoghmeRailT50Quant = int(math.ceil(((((new_valueb8 + new_valueb9 + new_valueb10) / 1.7) * 2) + 4))) * 2
        Pitch8Quantity = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(2 * int(LeftBracketWazneQuant))}</div>
                                        """
        st.markdown(Pitch8Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        LasticDescription = f"""
                                   <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['H2'].value}</div>
                                   """
        st.markdown(LasticDescription, unsafe_allow_html=True)
    with cols[1]:
        LasticQuantity = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 4}</div>
                                        """
        st.markdown(LasticQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value or ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value:
            SimBoxelScore10Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I2'].value}</div>
                    """
            st.markdown(SimBoxelScore10Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valuec3 or new_valueb3 == new_valued3 or new_valueb3 == new_valuee3:
            # SimBoxelScore10Quantity = f"""
            # <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(int(new_valueb2))*int(round((new_valueb8 + new_valueb9 + 5) * 4))}</div>
            # """
            # st.markdown(SimBoxelScore10Quantity, unsafe_allow_html=True)
            SimBoxelScore10Quantity = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(int(new_valueb2)) * int(round(((new_valueb8 + 9) - 2) * 4))}</div>
                        """
            st.markdown(SimBoxelScore10Quantity, unsafe_allow_html=True)
        elif new_valueb3 == new_valuef3 or new_valueb3 == new_valueg3:
            SimBoxelScore10Quantity = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(int(new_valueb2)) * int(round(((new_valueb8 + 9) - 2) * 5))}</div>
                                    """
            st.markdown(SimBoxelScore10Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    # with cols[0]:
    #     if ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value:
    #         SimBoxelScore11Description = f"""
    #                     <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I5'].value}</div>
    #                     """
    #         st.markdown(SimBoxelScore11Description, unsafe_allow_html=True)
    # with cols[1]:
    #     if new_valueb3 == new_valuef3 or new_valueb3 == new_valueg3:
    #         SimBoxelScore11Quantity = f"""
    #             <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(int(new_valueb2)) * int(round(((new_valueb8 + 9) - 2) * 6))}</div>
    #             """
    #         st.markdown(SimBoxelScore11Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            SimBoxelScore12Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I3'].value}</div>
                    """
            st.markdown(SimBoxelScore12Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valueh3 or new_valueb3 == new_valuei3 or new_valueb3 == new_valuej3 or new_valueb3 == new_valuek3 or new_valueb3 == new_valuel3:
            SimBoxelScore12Quantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(int(new_valueb2)) * int(round(((new_valueb8 + 9) - 2) * 6))}</div>
            """
            st.markdown(SimBoxelScore12Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        SimBoxelScore6Description = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['I4'].value}</div>
                                    """
        st.markdown(SimBoxelScore6Description, unsafe_allow_html=True)
    with cols[1]:
        SimBoxelScore6Quantity = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(int(new_valueb2)) * int(math.ceil((new_valueb10 + new_valueb9) + ((new_valueb6 - 1) * 3.4) + 2)) * 2}</div>
                            """
        st.markdown(SimBoxelScore6Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        SteelRopeLengthDescription = f"""
                                   <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AZ1'].value}</div>
                                   """
        st.markdown(SteelRopeLengthDescription, unsafe_allow_html=True)
    with cols[1]:
        SteelRopeLengthQuantity = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * ((new_valueb10 * 2) + 8 + new_valueb21)} m</div>
                                        """
        st.markdown(SteelRopeLengthQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value or ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value:
            GholabBoxelScore10Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J2'].value}</div>
                    """
            st.markdown(GholabBoxelScore10Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valuec3 or new_valueb3 == new_valued3 or new_valueb3 == new_valuee3:
            GholabBoxelScore10Quantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(int(new_valueb2)) * int((new_valueb17) * 2)}</div>
            """
            st.markdown(GholabBoxelScore10Quantity, unsafe_allow_html=True)
        if new_valueb3 == new_valuef3 or new_valueb3 == new_valueg3:
            GholabBoxelScore10Quantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(int(new_valueb2)) * int((new_valueb17) * 2)}</div>
            """
            st.markdown(GholabBoxelScore10Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            GholabBoxelScore13Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['J3'].value}</div>
                    """
            st.markdown(GholabBoxelScore13Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valueh3 or new_valueb3 == new_valuei3 or new_valueb3 == new_valuej3 or new_valueb3 == new_valuek3 or new_valueb3 == new_valuel3:
            GholabBoxelScore13Quantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(int(new_valueb2)) * int((new_valueb17) * 2)}</div>
            """
            st.markdown(GholabBoxelScore13Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value:
            FalakeHarzgard404Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K2'].value}</div>
                    """
            st.markdown(FalakeHarzgard404Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valuec3 or new_valueb3 == new_valued3 or new_valueb3 == new_valuee3:
            FalakeHarzgard404Quantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(FalakeHarzgard404Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value:
            FalakeHarzgard405Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K3'].value}</div>
                    """
            st.markdown(FalakeHarzgard405Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valuef3 or new_valueb3 == new_valueg3:
            FalakeHarzgard405Quantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(FalakeHarzgard405Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            FalakeHarzgard485Description = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['K4'].value}</div>
                    """
            st.markdown(FalakeHarzgard485Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valueh3 or new_valueb3 == new_valuei3 or new_valueb3 == new_valuej3 or new_valueb3 == new_valuek3 or new_valueb3 == new_valuel3:
            FalakeHarzgard485Quantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(FalakeHarzgard485Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if new_valueb5 == new_valuec5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valuec19: 
            GovernorUpDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L2'].value}</div>
                            """
            st.markdown(GovernorUpDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valued5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valuec19: 
            GovernorUpDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L4'].value}</div>
                            """
            st.markdown(GovernorUpDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valuec5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valued19 and new_valueb20 == new_valuec20: 
            GovernorUpDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L6'].value}</div>
                            """
            st.markdown(GovernorUpDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valuec5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valued19 and new_valueb20 != new_valuec20: 
            GovernorUpDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L10'].value}</div>
                            """
            st.markdown(GovernorUpDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valued5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valued19 and new_valueb20 == new_valuec20: 
            GovernorUpDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L8'].value}</div>
                            """
            st.markdown(GovernorUpDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valued5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valued19 and new_valueb20 != new_valuec20: 
            GovernorUpDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L12'].value}</div>
                            """
            st.markdown(GovernorUpDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valuec5 and new_valueb18 == new_valued18:
            GovernorUpDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L14'].value}</div>
                            """
            st.markdown(GovernorUpDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valued5 and new_valueb18 == new_valued18:
            GovernorUpDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L16'].value}</div>
                            """
            st.markdown(GovernorUpDescription, unsafe_allow_html=True)
    with cols[1]:
        GovernorUpQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                """
        st.markdown(GovernorUpQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if new_valueb5 == new_valuec5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valuec19: 
            GovernorDownDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L3'].value}</div>
                            """
            st.markdown(GovernorDownDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valued5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valuec19: 
            GovernorDownDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L5'].value}</div>
                            """
            st.markdown(GovernorDownDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valuec5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valued19 and new_valueb20 == new_valuec20: 
            GovernorDownDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L7'].value}</div>
                            """
            st.markdown(GovernorDownDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valuec5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valued19 and new_valueb20 != new_valuec20: 
            GovernorDownDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L11'].value}</div>
                            """
            st.markdown(GovernorDownDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valued5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valued19 and new_valueb20 == new_valuec20: 
            GovernorDownDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L9'].value}</div>
                            """
            st.markdown(GovernorDownDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valued5 and new_valueb18 == new_valuec18 and new_valueb19 == new_valued19 and new_valueb20 != new_valuec20: 
            GovernorDownDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L13'].value}</div>
                            """
            st.markdown(GovernorDownDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valuec5 and new_valueb18 == new_valued18:
            GovernorDownDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L15'].value}</div>
                            """
            st.markdown(GovernorDownDescription, unsafe_allow_html=True)
        elif new_valueb5 == new_valued5 and new_valueb18 == new_valued18:
            GovernorDownDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['L17'].value}</div>
                            """
            st.markdown(GovernorDownDescription, unsafe_allow_html=True)
    with cols[1]:
        GovernorDownQuantity = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                        """
        st.markdown(GovernorDownQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B11'].value == ws1['D11'].value and ws1['B13'].value == ws1['C13'].value:
            LeftDoorGhoflDescription = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M2'].value}</div>
                                    """
            st.markdown(LeftDoorGhoflDescription, unsafe_allow_html=True)
        elif ws1['B11'].value == ws1['D11'].value and ws1['B13'].value == ws1['D13'].value:
            RightDoorGhoflDescription = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['M3'].value}</div>
                                    """
            st.markdown(RightDoorGhoflDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb11 == new_valued11 and new_valueb13 == new_valuec13:
            LeftDoorGhoflQuantity = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{int(new_valueb2 * new_valueb6)}</div>
                                    """
            st.markdown(LeftDoorGhoflQuantity, unsafe_allow_html=True)
        elif new_valueb11 == new_valued11 and new_valueb13 == new_valued13:
            RightDoorGhoflQuantity = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{int(new_valueb2 * new_valueb6)}</div>
                                    """
            st.markdown(RightDoorGhoflQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B11'].value == ws1['D11'].value and ws1['B13'].value == ws1['C13'].value:
            DictatorDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N2'].value}</div>
                                """
            st.markdown(DictatorDescription, unsafe_allow_html=True)
        elif ws1['B11'].value == ws1['D11'].value and ws1['B13'].value == ws1['D13'].value:
            DictatorDescription = f"""
                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['N2'].value}</div>
                                            """
            st.markdown(DictatorDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb11 == new_valued11 and new_valueb13 == new_valuec13:
            DictatorQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{int(new_valueb2 * new_valueb6)}</div>
                                """
            st.markdown(DictatorQuantity, unsafe_allow_html=True)
        elif new_valueb11 == new_valued11 and new_valueb13 == new_valued13:
            DictatorQuantity = f"""
                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{int(new_valueb2 * new_valueb6)}</div>
                                            """
            st.markdown(DictatorQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        DoorKeyDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['O2'].value}</div>
                                """
        st.markdown(DoorKeyDescription, unsafe_allow_html=True)
    with cols[1]:
        DoorKeyQuantity = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                        """
        st.markdown(DoorKeyQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value:
            PolyortanDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P2'].value}</div>
                    """
            st.markdown(PolyortanDescription, unsafe_allow_html=True)
        elif ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value:
            PolyortanDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['P3'].value}</div>
                    """
            st.markdown(PolyortanDescription, unsafe_allow_html=True)
        elif ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            BufferDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Q2'].value}</div>
                            """
            st.markdown(BufferDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valuec3 or new_valueb3 == new_valued3 or new_valueb3 == new_valuee3:
            PolyortanQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
            """
            st.markdown(PolyortanQuantity, unsafe_allow_html=True)
        elif new_valueb3 == new_valuef3 or new_valueb3 == new_valueg3:
            PolyortanQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
            """
            st.markdown(PolyortanQuantity, unsafe_allow_html=True)
        elif new_valueb3 == new_valueh3 or new_valueb3 == new_valuei3 or new_valueb3 == new_valuej3 or new_valueb3 == new_valuek3 or new_valueb3 == new_valuel3:
            BufferQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
            """
            st.markdown(BufferQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        RoghandanDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['R2'].value}</div>
                                """
        st.markdown(RoghandanDescription, unsafe_allow_html=True)
    with cols[1]:
        RoghandanQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 4}</div>
                """
        st.markdown(RoghandanQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        AshkiDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['S2'].value}</div>
                                """
        st.markdown(AshkiDescription, unsafe_allow_html=True)
    with cols[1]:
        AshkiQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                """
        st.markdown(AshkiQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        CorpiScore6Description = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['T2'].value}</div>
                                """
        st.markdown(CorpiScore6Description, unsafe_allow_html=True)
    with cols[1]:
        CorpiScore6Quantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 6}</div>
                """
        st.markdown(CorpiScore6Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value:
            CorpiScore10Description = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['T3'].value}</div>
                                    """
            st.markdown(CorpiScore10Description, unsafe_allow_html=True)
        elif ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value:
            CorpiScore10Description = f"""
                                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['T3'].value}</div>
                                                """
            st.markdown(CorpiScore10Description, unsafe_allow_html=True)
            # CorpiScore11Description = f"""
            #                         <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['T5'].value}</div>
            #                         """
            # st.markdown(CorpiScore11Description, unsafe_allow_html=True)
        elif ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            CorpiScore12Description = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['T4'].value}</div>
                                    """
            st.markdown(CorpiScore12Description, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valuec3 or new_valueb3 == new_valued3 or new_valueb3 == new_valuee3:
            # SimBoxelScore10Quant = (int(new_valueb2)) * int(round(((new_valueb8 + 9) - 2) * 4))
            CorpiScore10Quantity = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) *int((new_valueb17) * 4)}</div>
                    """
            st.markdown(CorpiScore10Quantity, unsafe_allow_html=True)
        elif new_valueb3 == new_valuef3 or new_valueb3 == new_valueg3:
            # SimBoxelScore10Quant = (int(new_valueb2)) * int(round(((new_valueb8 + 9) - 2) * 5))
            CorpiScore10Quantity = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) *int((new_valueb17) * 4)}</div>
                    """
            st.markdown(CorpiScore10Quantity, unsafe_allow_html=True)
            # SimBoxelScore11Quant = (int(new_valueb2)) * int(round(((new_valueb8 + 9) - 2) * 6))
            # CorpiScore11Quantity = f"""
            #                     <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(SimBoxelScore11Quant) * 4}</div>
            #                     """
            # st.markdown(CorpiScore11Quantity, unsafe_allow_html=True)
        elif new_valueb3 == new_valueh3 or new_valueb3 == new_valuei3 or new_valueb3 == new_valuej3 or new_valueb3 == new_valuek3 or new_valueb3 == new_valuel3:
            # SimBoxelScore12Quant = (int(new_valueb2)) * int(round(((new_valueb8 + 9) - 2) * 6))
            CorpiScore12Quantity = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) *int((new_valueb17) * 4)}</div>
                    """
            st.markdown(CorpiScore12Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        PitchDescription = f"""
                                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['U2'].value}</div>
                                                """
        st.markdown(PitchDescription, unsafe_allow_html=True)
    with cols[1]:
        PitchQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                """
        st.markdown(PitchQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value:
            TabloFarmanDescription = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['V2'].value}</div>
                        """
            st.markdown(TabloFarmanDescription, unsafe_allow_html=True)
        elif ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value:
            TabloFarmanDescription = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['V3'].value}</div>
                        """
            st.markdown(TabloFarmanDescription, unsafe_allow_html=True)
        elif ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            TabloFarmanDescription = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['V4'].value}</div>
                        """
            st.markdown(TabloFarmanDescription, unsafe_allow_html=True)
    with cols[1]:
        TabloFarmanQuantity = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                    """
        st.markdown(TabloFarmanQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        TabloBarghDescription = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['W2'].value}</div>
                                        """
        st.markdown(TabloBarghDescription, unsafe_allow_html=True)
    with cols[1]:
        TabloBarghQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                """
        st.markdown(TabloBarghQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value:
            UPSDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['X2'].value}</div>
                            """
            st.markdown(UPSDescription, unsafe_allow_html=True)
        elif ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value:
            UPSDescription = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['X3'].value}</div>
                                        """
            st.markdown(UPSDescription, unsafe_allow_html=True)
        elif ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            UPSDescription = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['X4'].value}</div>
                                        """
            st.markdown(UPSDescription, unsafe_allow_html=True)
    with cols[1]:
        UPSQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                """
        st.markdown(UPSQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        # if ws1['B11'].value == ws1['D11'].value:
        #     PhotocellDescription = f"""
        #                     <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Y2'].value}</div>
        #                     """
        #     st.markdown(PhotocellDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value:
            PhotocellDescription = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Y3'].value}</div>
                            """
            st.markdown(PhotocellDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb11 == new_valuec11:
            PhotocellQuantity = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                    """
            st.markdown(PhotocellQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        CabinDoorShasiDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Z2'].value}</div>
                                """
        st.markdown(CabinDoorShasiDescription, unsafe_allow_html=True)
    with cols[1]:
        CabinDoorShasiQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                """
        st.markdown(CabinDoorShasiQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        LandingShasiDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['Z3'].value}</div>
                                """
        st.markdown(LandingShasiDescription, unsafe_allow_html=True)
    with cols[1]:
        LandingShasiQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2 * new_valueb6)}</div>
                """
        st.markdown(LandingShasiQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        TravelCableDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AA2'].value}</div>
                                """
        st.markdown(TravelCableDescription, unsafe_allow_html=True)
    with cols[1]:
        TravelCableQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{(int(new_valueb2)) * int(math.ceil(new_valueb8 + 5 + new_valueb9 + 3) + 1)}</div>
                """
        st.markdown(TravelCableQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        ElectrosignalDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AB2'].value}</div>
                                """
        st.markdown(ElectrosignalDescription, unsafe_allow_html=True)
    with cols[1]:
        ElectrosignalQuantity = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                        """
        st.markdown(ElectrosignalQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        ShalterDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AC2'].value}</div>
                                """
        st.markdown(ShalterDescription, unsafe_allow_html=True)
    with cols[1]:
        ShalterQuantity = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*2}</div>
                        """
        st.markdown(ShalterQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        OverloadDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AD2'].value}</div>
                                """
        st.markdown(OverloadDescription, unsafe_allow_html=True)
    with cols[1]:
        OverloadQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                                """
        st.markdown(OverloadQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        TunnelLightDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AE2'].value}</div>
                                """
        st.markdown(TunnelLightDescription, unsafe_allow_html=True)
    with cols[1]:
        # TunnelLightQuantity = f"""
        #                         <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2 * new_valueb6 * 2)}</div>
        #                         """
        # st.markdown(TunnelLightQuantity, unsafe_allow_html=True)
        TunnelLightQuantity = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2 * new_valueb6)}</div>
                                        """
        st.markdown(TunnelLightQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        Simafshan6Description = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AF2'].value}</div>
                                """
        st.markdown(Simafshan6Description, unsafe_allow_html=True)
    with cols[1]:
        Simafshan6Quantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(math.ceil(new_valueb8 + new_valueb9 + new_valueb10 + 5))}</div>
                                     """
        st.markdown(Simafshan6Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        Simafshan4Description = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AF3'].value}</div>
                                        """
        st.markdown(Simafshan4Description, unsafe_allow_html=True)
    with cols[1]:
        Simafshan4Quantity = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                                             """
        st.markdown(Simafshan4Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B6'].value != ws1['C6'].value:
            SimafshanBlueDescription = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AF4'].value}</div>
                                    """
            st.markdown(SimafshanBlueDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb6 == new_valued6:
            SimafshanBlueQuantity = f"""
                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                                                 """
            st.markdown(SimafshanBlueQuantity, unsafe_allow_html=True)
        elif new_valueb6 != new_valuec6 and new_valueb6 != new_valued6:
            SimafshanBlueQuantity = f"""
                                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                                                             """
            st.markdown(SimafshanBlueQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        SimafshanYellowDescription = f"""
                                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AF5'].value}</div>
                                                        """
        st.markdown(SimafshanYellowDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb6 == new_valuec6 or new_valueb6 == new_valued6 or new_valueb6 == new_valuee6:
            SimafshanYellowQuantity = f"""
                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                                                 """
            st.markdown(SimafshanYellowQuantity, unsafe_allow_html=True)
        else:
            SimafshanYellowQuantity = f"""
                                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                                                             """
            st.markdown(SimafshanYellowQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        SimafshanGreenDescription = f"""
                                                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AF6'].value}</div>
                                                                """
        st.markdown(SimafshanGreenDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb6 == new_valuec6 or new_valueb6 == new_valued6 or new_valueb6 == new_valuee6 or new_valueb6 == new_valuef6:
            SimafshanGreenQuantity = f"""
                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                                                 """
            st.markdown(SimafshanGreenQuantity, unsafe_allow_html=True)
        else:
            SimafshanGreenQuantity = f"""
                                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                                                             """
            st.markdown(SimafshanGreenQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        SimafshanRedDescription = f"""
                                                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AF7'].value}</div>
                                                                """
        st.markdown(SimafshanRedDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb6 == new_valuec6 or new_valueb6 == new_valued6 or new_valueb6 == new_valuee6 or new_valueb6 == new_valuef6 or new_valueb6 == new_valueg6:
            SimafshanRedQuantity = f"""
                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                                                 """
            st.markdown(SimafshanRedQuantity, unsafe_allow_html=True)
        else:
            SimafshanRedQuantity = f"""
                                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                                                             """
            st.markdown(SimafshanRedQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        SimafshanBlackDescription = f"""
                                                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AF8'].value}</div>
                                                                """
        st.markdown(SimafshanBlackDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb6 == new_valuec6 or new_valueb6 == new_valued6 or new_valueb6 == new_valuee6 or new_valueb6 == new_valuef6 or new_valueb6 == new_valueg6 or new_valueb6 == new_valueh6:
            SimafshanBlackQuantity = f"""
                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                                                 """
            st.markdown(SimafshanBlackQuantity, unsafe_allow_html=True)
        else:
            SimafshanBlackQuantity = f"""
                                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                                                             """
            st.markdown(SimafshanBlackQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        TunnelLightCableDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AG2'].value}</div>
                                """
        st.markdown(TunnelLightCableDescription, unsafe_allow_html=True)
    with cols[1]:
        TunnelLightCableQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(math.ceil(new_valueb8 + new_valueb9 + new_valueb10 + 5))}</div>
                                """
        st.markdown(TunnelLightCableQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        Dockt9Description = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AH2'].value}</div>
                                """
        st.markdown(Dockt9Description, unsafe_allow_html=True)
    with cols[1]:
        Dockt9Quantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                                """
        st.markdown(Dockt9Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        Dockt3Description = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AH3'].value}</div>
                                        """
        st.markdown(Dockt3Description, unsafe_allow_html=True)
    with cols[1]:
        Dockt3Quantity = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(math.ceil(((new_valueb8 + new_valueb9 + new_valueb10) / 2) - 1))}</div>
                                        """
        st.markdown(Dockt3Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        Dockt10Description = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AH4'].value}</div>
                                        """
        st.markdown(Dockt10Description, unsafe_allow_html=True)
    with cols[1]:
        Dockt10Quantity = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                                        """
        st.markdown(Dockt10Quantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        LoleKhortomiFeleziDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AI2'].value}</div>
                                """
        st.markdown(LoleKhortomiFeleziDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb6 == new_valuec6 or new_valueb6 == new_valued6 or new_valueb6 == new_valuee6:
            LoleKhortomiFeleziQuantity = f"""
                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                            """
            st.markdown(LoleKhortomiFeleziQuantity, unsafe_allow_html=True)
        else:
            LoleKhortomiFeleziQuantity = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 3}</div>
                                    """
            st.markdown(LoleKhortomiFeleziQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        LoleKhortomiPlasticiDescription = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AI3'].value}</div>
                                        """
        st.markdown(LoleKhortomiPlasticiDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb6 == new_valuec6 or new_valueb6 == new_valued6 or new_valueb6 == new_valuee6:
            LoleKhortomiPlasticiQuantity = f"""
                                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                                    """
            st.markdown(LoleKhortomiPlasticiQuantity, unsafe_allow_html=True)
        else:
            LoleKhortomiPlasticiQuantity = f"""
                                            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 3}</div>
                                            """
            st.markdown(LoleKhortomiPlasticiQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        PrizRokarDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AJ2'].value}</div>
                                """
        st.markdown(PrizRokarDescription, unsafe_allow_html=True)
    with cols[1]:
        PrizRokarQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                                """
        st.markdown(PrizRokarQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        TabdilKeyDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AK2'].value}</div>
                                """
        st.markdown(TabdilKeyDescription, unsafe_allow_html=True)
    with cols[1]:
        TabdilKeyQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)*2}</div>
                                """
        st.markdown(TabdilKeyQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        GharchiKeyDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AL2'].value}</div>
                                """
        st.markdown(GharchiKeyDescription, unsafe_allow_html=True)
    with cols[1]:
        GharchiKeyQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                                """
        st.markdown(GharchiKeyQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        GharchiKeyGhabDescription = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AL3'].value}</div>
                                        """
        st.markdown(GharchiKeyGhabDescription, unsafe_allow_html=True)
    with cols[1]:
        GharchiKeyGhabQuantity = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                                        """
        st.markdown(GharchiKeyGhabQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        MagnetDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AM2'].value}</div>
                                """
        st.markdown(MagnetDescription, unsafe_allow_html=True)
    with cols[1]:
        MagnetQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 5}</div>
                                """
        st.markdown(MagnetQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        NavarChasbDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AN2'].value}</div>
                                """
        st.markdown(NavarChasbDescription, unsafe_allow_html=True)
    with cols[1]:
        NavarChasbQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 10}</div>
                                """
        st.markdown(NavarChasbQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        BastTravelCableDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AO2'].value}</div>
                                """
        st.markdown(BastTravelCableDescription, unsafe_allow_html=True)
    with cols[1]:
        BastTravelCableQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 4}</div>
                                """
        st.markdown(BastTravelCableQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        BastKamarbandiDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AO3'].value}</div>
                                """
        st.markdown(BastKamarbandiDescription, unsafe_allow_html=True)
    with cols[1]:
        BastKamarbandiQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                                """
        st.markdown(BastKamarbandiQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['C12'].value and ws1['B13'].value == ws1['C13'].value:
            CabinDoorFull70LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP2'].value}</div>
                    """
            st.markdown(CabinDoorFull70LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['C12'].value and ws1['B13'].value == ws1['D13'].value:
            CabinDoorFull70RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP3'].value}</div>
                    """
            st.markdown(CabinDoorFull70RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['C12'].value and ws1['B13'].value == ws1['E13'].value:
            CabinDoorFull70CentralDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP4'].value}</div>
                    """
            st.markdown(CabinDoorFull70CentralDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['D12'].value and ws1['B13'].value == ws1['C13'].value:
            CabinDoorFull80LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP5'].value}</div>
                    """
            st.markdown(CabinDoorFull80LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['D12'].value and ws1['B13'].value == ws1['D13'].value:
            CabinDoorFull80RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP6'].value}</div>
                    """
            st.markdown(CabinDoorFull80RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['D12'].value and ws1['B13'].value == ws1['E13'].value:
            CabinDoorFull80CentralDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP7'].value}</div>
                    """
            st.markdown(CabinDoorFull80CentralDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['E12'].value and ws1['B13'].value == ws1['C13'].value:
            CabinDoorFull90LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP8'].value}</div>
                    """
            st.markdown(CabinDoorFull90LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['E12'].value and ws1['B13'].value == ws1['D13'].value:
            CabinDoorFull90RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP9'].value}</div>
                    """
            st.markdown(CabinDoorFull90RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['E12'].value and ws1['B13'].value == ws1['E13'].value:
            CabinDoorFull90CentralDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP10'].value}</div>
                    """
            st.markdown(CabinDoorFull90CentralDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['F12'].value and ws1['B13'].value == ws1['C13'].value:
            CabinDoorFull100LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP11'].value}</div>
                    """
            st.markdown(CabinDoorFull100LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['F12'].value and ws1['B13'].value == ws1['D13'].value:
            CabinDoorFull100RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP12'].value}</div>
                    """
            st.markdown(CabinDoorFull100RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['F12'].value and ws1['B13'].value == ws1['E13'].value:
            CabinDoorFull100CentralDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP13'].value}</div>
                    """
            st.markdown(CabinDoorFull100CentralDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['C12'].value and ws1['B13'].value == ws1['C13'].value:
            CabinDoorNime70LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP14'].value}</div>
                    """
            st.markdown(CabinDoorNime70LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['C12'].value and ws1['B13'].value == ws1['D13'].value:
            CabinDoorNime70RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP15'].value}</div>
                    """
            st.markdown(CabinDoorNime70RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['D12'].value and ws1['B13'].value == ws1['C13'].value:
            CabinDoorNime80LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP16'].value}</div>
                    """
            st.markdown(CabinDoorNime80LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['D12'].value and ws1['B13'].value == ws1['D13'].value:
            CabinDoorNime80RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP17'].value}</div>
                    """
            st.markdown(CabinDoorNime80RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['E12'].value and ws1['B13'].value == ws1['C13'].value:
            CabinDoorNime90LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP18'].value}</div>
                    """
            st.markdown(CabinDoorNime90LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['E12'].value and ws1['B13'].value == ws1['D13'].value:
            CabinDoorNime90RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AP19'].value}</div>
                    """
            st.markdown(CabinDoorNime90RightDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuec12 and new_valueb13 == new_valuec13:
            CabinDoorFull70LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull70LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuec12 and new_valueb13 == new_valued13:
            CabinDoorFull70RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull70RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuec12 and new_valueb13 == new_valuee13:
            CabinDoorFull70CentralQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull70CentralQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valued12 and new_valueb13 == new_valuec13:
            CabinDoorFull80LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull80LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valued12 and new_valueb13 == new_valued13:
            CabinDoorFull80RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull80RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valued12 and new_valueb13 == new_valuee13:
            CabinDoorFull80CentralQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull80CentralQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuee12 and new_valueb13 == new_valuec13:
            CabinDoorFull90LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull90LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuee12 and new_valueb13 == new_valued13:
            CabinDoorFull90RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull90RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuee12 and new_valueb13 == new_valuee13:
            CabinDoorFull90CentralQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull90CentralQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuef12 and new_valueb13 == new_valuec13:
            CabinDoorFull100LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull100LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuef12 and new_valueb13 == new_valued13:
            CabinDoorFull100RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull100RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuef12 and new_valueb13 == new_valuee13:
            CabinDoorFull100CentralQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorFull100CentralQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valuec12 and new_valueb13 == new_valuec13:
            CabinDoorNime70LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorNime70LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valuec12 and new_valueb13 == new_valued13:
            CabinDoorNime70RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorNime70RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valued12 and new_valueb13 == new_valuec13:
            CabinDoorNime80LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorNime80LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valued12 and new_valueb13 == new_valued13:
            CabinDoorNime80RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorNime80RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valuee12 and new_valueb13 == new_valuec13:
            CabinDoorNime90LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorNime90LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valuee12 and new_valueb13 == new_valued13:
            CabinDoorNime90RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
            """
            st.markdown(CabinDoorNime90RightQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['C12'].value and ws1['B13'].value == ws1['C13'].value:
            LandingDoorFull70LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ2'].value}</div>
                    """
            st.markdown(LandingDoorFull70LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['C12'].value and ws1['B13'].value == ws1['D13'].value:
            LandingDoorFull70RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ3'].value}</div>
                    """
            st.markdown(LandingDoorFull70RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['C12'].value and ws1['B13'].value == ws1['E13'].value:
            LandingDoorFull70CentralDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ4'].value}</div>
                    """
            st.markdown(LandingDoorFull70CentralDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['D12'].value and ws1['B13'].value == ws1['C13'].value:
            LandingDoorFull80LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ5'].value}</div>
                    """
            st.markdown(LandingDoorFull80LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['D12'].value and ws1['B13'].value == ws1['D13'].value:
            LandingDoorFull80RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ6'].value}</div>
                    """
            st.markdown(LandingDoorFull80RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['D12'].value and ws1['B13'].value == ws1['E13'].value:
            LandingDoorFull80CentralDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ7'].value}</div>
                    """
            st.markdown(LandingDoorFull80CentralDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['E12'].value and ws1['B13'].value == ws1['C13'].value:
            LandingDoorFull90LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ8'].value}</div>
                    """
            st.markdown(LandingDoorFull90LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['E12'].value and ws1['B13'].value == ws1['D13'].value:
            LandingDoorFull90RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ9'].value}</div>
                    """
            st.markdown(LandingDoorFull90RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['E12'].value and ws1['B13'].value == ws1['E13'].value:
            LandingDoorFull90CentralDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ10'].value}</div>
                    """
            st.markdown(LandingDoorFull90CentralDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['F12'].value and ws1['B13'].value == ws1['C13'].value:
            LandingDoorFull100LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ11'].value}</div>
                    """
            st.markdown(LandingDoorFull100LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['F12'].value and ws1['B13'].value == ws1['D13'].value:
            LandingDoorFull100RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ12'].value}</div>
                    """
            st.markdown(LandingDoorFull100RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['C11'].value and ws1['B12'].value == ws1['F12'].value and ws1['B13'].value == ws1['E13'].value:
            LandingDoorFull100CentralDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ13'].value}</div>
                    """
            st.markdown(LandingDoorFull100CentralDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['C12'].value and ws1['B13'].value == ws1['C13'].value:
            LandingDoorNime70LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ14'].value}</div>
                    """
            st.markdown(LandingDoorNime70LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['C12'].value and ws1['B13'].value == ws1['D13'].value:
            LandingDoorNime70RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ15'].value}</div>
                    """
            st.markdown(LandingDoorNime70RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['D12'].value and ws1['B13'].value == ws1['C13'].value:
            LandingDoorNime80LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ16'].value}</div>
                    """
            st.markdown(LandingDoorNime80LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['D12'].value and ws1['B13'].value == ws1['D13'].value:
            LandingDoorNime80RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ17'].value}</div>
                    """
            st.markdown(LandingDoorNime80RightDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['E12'].value and ws1['B13'].value == ws1['C13'].value:
            LandingDoorNime90LeftDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ18'].value}</div>
                    """
            st.markdown(LandingDoorNime90LeftDescription, unsafe_allow_html=True)
        if ws1['B11'].value == ws1['D11'].value and ws1['B12'].value == ws1['E12'].value and ws1['B13'].value == ws1['D13'].value:
            LandingDoorNime90RightDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AQ19'].value}</div>
                    """
            st.markdown(LandingDoorNime90RightDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuec12 and new_valueb13 == new_valuec13:
            LandingDoorFull70LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull70LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuec12 and new_valueb13 == new_valued13:
            LandingDoorFull70RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull70RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuec12 and new_valueb13 == new_valuee13:
            LandingDoorFull70CentralQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull70CentralQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valued12 and new_valueb13 == new_valuec13:
            LandingDoorFull80LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull80LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valued12 and new_valueb13 == new_valued13:
            LandingDoorFull80RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull80RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valued12 and new_valueb13 == new_valuee13:
            LandingDoorFull80CentralQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull80CentralQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuee12 and new_valueb13 == new_valuec13:
            LandingDoorFull90LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull90LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuee12 and new_valueb13 == new_valued13:
            LandingDoorFull90RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull90RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuee12 and new_valueb13 == new_valuee13:
            LandingDoorFull90CentralQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull90CentralQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuef12 and new_valueb13 == new_valuec13:
            LandingDoorFull100LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull100LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuef12 and new_valueb13 == new_valued13:
            LandingDoorFull100RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull100RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valuec11 and new_valueb12 == new_valuef12 and new_valueb13 == new_valuee13:
            LandingDoorFull100CentralQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorFull100CentralQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valuec12 and new_valueb13 == new_valuec13:
            LandingDoorNime70LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorNime70LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valuec12 and new_valueb13 == new_valued13:
            LandingDoorNime70RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorNime70RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valued12 and new_valueb13 == new_valuec13:
            LandingDoorNime80LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorNime80LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valued12 and new_valueb13 == new_valued13:
            LandingDoorNime80RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorNime80RightQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valuee12 and new_valueb13 == new_valuec13:
            LandingDoorNime90LeftQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorNime90LeftQuantity, unsafe_allow_html=True)
        if new_valueb11 == new_valued11 and new_valueb12 == new_valuee12 and new_valueb13 == new_valued13:
            LandingDoorNime90RightQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb6)}</div>
            """
            st.markdown(LandingDoorNime90RightQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value:
            ShasiDescription = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AR2'].value}</div>
            """
            st.markdown(ShasiDescription, unsafe_allow_html=True)
        elif ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value:
            ShasiDescription = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AR3'].value}</div>
            """
            st.markdown(ShasiDescription, unsafe_allow_html=True)
        elif ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value or ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value:
            ShasiDescription = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AR4'].value}</div>
            """
            st.markdown(ShasiDescription, unsafe_allow_html=True)
    with cols[1]:
        ShasiQuantity = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                        """
        st.markdown(ShasiQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if (ws1['B14'].value == ws1['C14'].value) and (ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS2'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['C14'].value) and (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS2'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['C14'].value) and (ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS3'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['C14'].value) and (ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS3'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['D14'].value) and (ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS4'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['D14'].value) and (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS4'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['D14'].value) and (ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS5'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['D14'].value) and (ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS5'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['E14'].value) and (ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS6'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['E14'].value) and (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS6'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['E14'].value) and (ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS7'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['E14'].value) and (ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value):
            WazneTadolDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS7'].value}</div>
                    """
            st.markdown(WazneTadolDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb14 == new_valuec14 and new_valueb3 == new_valuec3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuec3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valued3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valued3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuee3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuee3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuef3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuef3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valueg3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valueg3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valueh3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valueh3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuei3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuei3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuej3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuej3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuek3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuek3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuel3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuel3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuec3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuec3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valued3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valued3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuee3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuee3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuef3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuef3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valueg3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valueg3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valueh3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valueh3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuei3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuei3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuej3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuej3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuek3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuek3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuel3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuel3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuec3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuec3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valued3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valued3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuee3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuee3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuef3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuef3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valueg3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valueg3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valueh3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valueh3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuei3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuei3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuej3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuej3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuek3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuek3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuel3:
            WazneTadolQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int(new_valueb16 + (0.5 * 75 * new_valuel3) - 75)} kg</div>
            """
            st.markdown(WazneTadolQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        if (ws1['B14'].value == ws1['C14'].value) and (ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['C14'].value) and (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['C14'].value) and (ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['C14'].value) and (ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['D14'].value) and (ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['D14'].value) and (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['D14'].value) and (ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['D14'].value) and (ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['E14'].value) and (ws1['B3'].value == ws1['C3'].value or ws1['B3'].value == ws1['D3'].value or ws1['B3'].value == ws1['E3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['E14'].value) and (ws1['B3'].value == ws1['F3'].value or ws1['B3'].value == ws1['G3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['E14'].value) and (ws1['B3'].value == ws1['H3'].value or ws1['B3'].value == ws1['I3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
        elif (ws1['B14'].value == ws1['E14'].value) and (ws1['B3'].value == ws1['J3'].value or ws1['B3'].value == ws1['K3'].value or ws1['B3'].value == ws1['L3'].value):
            WazneDescription = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AS8'].value}</div>
                    """
            st.markdown(WazneDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb14 == new_valuec14 and new_valueb3 == new_valuec3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuec3) - 75)/45)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valued3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valued3) - 75)/45)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuee3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuee3) - 75)/45)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuef3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuef3) - 75)/45)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valueg3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valueg3) - 75)/45)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valueh3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valueh3) - 75)/45)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuei3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuei3) - 75)/45)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuej3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuej3) - 75)/45)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuek3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuek3) - 75)/45)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuec14 and new_valueb3 == new_valuel3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuel3) - 75)/45)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuec3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuec3) - 75)/52)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valued3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valued3) - 75)/52)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuee3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuee3) - 75)/52)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuef3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuef3) - 75)/52)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valueg3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valueg3) - 75)/52)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valueh3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valueh3) - 75)/52)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuei3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuei3) - 75)/52)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuej3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuej3) - 75)/52)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuek3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuek3) - 75)/52)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valued14 and new_valueb3 == new_valuel3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuel3) - 75)/52)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuec3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuec3) - 75)/58)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valued3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valued3) - 75)/58)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuee3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuee3) - 75)/58)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuef3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuef3) - 75)/58)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valueg3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valueg3) - 75)/58)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valueh3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valueh3) - 75)/58)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuei3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuei3) - 75)/58)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuej3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuej3) - 75)/58)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuek3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuek3) - 75)/58)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
        elif new_valueb14 == new_valuee14 and new_valueb3 == new_valuel3:
            WazneQuantity = f"""
            <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * int((new_valueb16 + (0.5 * 75 * new_valuel3) - 75)/58)}</div>
            """
            st.markdown(WazneQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        HefazFalakeMotorDescription = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AT2'].value}</div>
                        """
        st.markdown(HefazFalakeMotorDescription, unsafe_allow_html=True)
    with cols[1]:
        HefazFalakeMotorQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                """
        st.markdown(HefazFalakeMotorQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        HefazGovernorDescription = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AT3'].value}</div>
                        """
        st.markdown(HefazGovernorDescription, unsafe_allow_html=True)
    with cols[1]:
        HefazGovernorQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                """
        st.markdown(HefazGovernorQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        HefazFalakeHarzgardDescription = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AT4'].value}</div>
                        """
        st.markdown(HefazFalakeHarzgardDescription, unsafe_allow_html=True)
    with cols[1]:
        HefazFalakeHarzgardQuantity = f"""
                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                """
        st.markdown(HefazFalakeHarzgardQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        PhoneDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AU2'].value}</div>
                                """
        st.markdown(PhoneDescription, unsafe_allow_html=True)
    with cols[1]:
        PhoneQuantity = f"""
                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                        """
        st.markdown(PhoneQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        BatteryDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AV2'].value}</div>
                                """
        st.markdown(BatteryDescription, unsafe_allow_html=True)
    with cols[1]:
        if new_valueb3 == new_valuec3 or new_valueb3 == new_valued3 or new_valueb3 == new_valuee3 or new_valueb3 == new_valuef3 or new_valueb3 == new_valueg3:
            BatteryQuantity = f"""
                    <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 2}</div>
                    """
            st.markdown(BatteryQuantity, unsafe_allow_html=True)
        else:
            BatteryQuantity = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2) * 3}</div>
                                """
            st.markdown(BatteryQuantity, unsafe_allow_html=True)
    cols = st.columns(2)
    with cols[0]:
        AghlamStandardDescription = f"""
                                <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;direction:rtl;'>{ws2['AW2'].value}</div>
                                """
        st.markdown(AghlamStandardDescription, unsafe_allow_html=True)
    with cols[1]:
        AghlamStandardQuantity = f"""
                                        <div style='background-color:#f0f0f0;padding:10px;border-radius:5px;display:block;margin-bottom:5px;height:60px;text-align:center;'>{int(new_valueb2)}</div>
                                        """
        st.markdown(AghlamStandardQuantity, unsafe_allow_html=True)









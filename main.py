import copy
import json
import os
import socket
import sys
import threading
import time
import pynput
import yaml
from PySide6.QtCore import Slot, QThread, Signal
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication, QTextBrowser

from YD_UI import Ui_MainWindow
from utils.Serial485_unit import Serial485
from utils.SportCard_unit import SportCard, card_res
from utils.tool_unit import succeed, fail, is_natural_num, check_network_with_ip
from utils.z_MySql import create_connection, fetch_query


def query_sql():
    # 创建数据库连接
    try:
        conn = create_connection("192.168.0.80", "root", "root", "dataini")

        if conn:
            local_ip = check_network_with_ip()

            # 查询配置表的 SQL 语句
            user_value = local_ip[1]  # 网卡号
            key_value = "电压输出%"  # 读取字段
            key_value2 = "网络摄像机%"  # 读取字段
            key_value3 = "赛道名称%"  # 读取字段
            key_value4 = "图像识别IP"  # 读取字段
            key_value5 = "全局配置.IP%"  # 读取字段
            key_value6 = "全局配置.驱动器端口"  # 读取字段
            key_values = ["电压输出"]
            port_values = ["全局配置.IP", "全局配置.驱动器端口"]
            # key_values = ["电压输出", "网络摄像机", "赛道名称", "图像识别IP", "全局配置.IP"]
            # select_query = "SELECT * FROM config WHERE `user`=%s AND `key`=%s"
            select_query = ("SELECT * FROM config WHERE `user`=%s "
                            "AND (`key` LIKE %s "
                            "OR `key` LIKE %s "
                            "OR `key` LIKE %s "
                            "OR `key` = %s "
                            "OR `key` LIKE %s "
                            "OR `key` LIKE %s)")
            res = fetch_query(conn, select_query,
                              [user_value,
                               key_value,
                               key_value2,
                               key_value3,
                               key_value4,
                               key_value5,
                               key_value6])
            # print("Query Results:", type(res), res)
            text_sql = {}
            text_port = {}
            for index in range(len(res)):
                for k in key_values:
                    if res[index][3] != '0' and (k in res[index][2]):
                        text_sql[res[index][2]] = res[index][3]
                for p in port_values:
                    if res[index][3] != '0' and (p in res[index][2]):
                        text_port[res[index][2]] = res[index][3]
            # 关闭连接
            conn.close()
            return text_sql, text_port
    except RuntimeError as e:
        print(f"Runtime error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def organ_shoot():  # 弹射开关
    if not flg_start['card']:
        return
    try:
        index = int(ui.lineEdit_shoot.text()) - 1
        if ui.checkBox_shoot.isChecked():
            sc.GASetExtDoBit(index, 1)
        else:
            sc.GASetExtDoBit(index, 0)
    except:
        print('运动卡电压输出错误！')
        ui.textBrowser.append(fail('运动卡电压输出错误！'))
        flg_start['card'] = False


def organ_start():  # 开启开关
    if not flg_start['card']:
        return
    try:
        index = int(ui.lineEdit_start.text()) - 1
        if ui.checkBox_start.isChecked():
            sc.GASetExtDoBit(index, 1)
        else:
            sc.GASetExtDoBit(index, 0)
    except:
        print('运动卡电压输出错误！')
        ui.textBrowser.append(fail('运动卡电压输出错误！'))
        flg_start['card'] = False


def organ_end():  # 结束开关
    if not flg_start['card']:
        return
    try:
        index = int(ui.lineEdit_end.text()) - 1
        if ui.checkBox_end.isChecked():
            sc.GASetExtDoBit(index, 1)
        else:
            sc.GASetExtDoBit(index, 0)
    except:
        print('运动卡电压输出错误！')
        ui.textBrowser.append(fail('运动卡电压输出错误！'))
        flg_start['card'] = False


def organ_number():  # 号码开关
    if not flg_start['card']:
        return
    try:
        index = int(ui.lineEdit_OutNo.text()) - 1
        if ui.checkBox_switch.isChecked():
            sc.GASetExtDoBit(index, 1)
        else:
            sc.GASetExtDoBit(index, 0)
    except:
        print('运动卡电压输出错误！')
        ui.textBrowser.append(fail('运动卡电压输出错误！'))
        flg_start['card'] = False


def card_start():
    if not CardStart_Thread.isRunning():
        CardStart_Thread.start()


def card_close_all():
    if not flg_start['card']:
        return
    for index in range(0, 16):
        sc.GASetExtDoBit(index, 0)
        time.sleep(0.1)
    ui.textBrowser.append(succeed('已经关闭所有机关！'))


def card_reset():
    Axis_Thread.run_flg = True


# 关闭动作循环
def cmd_stop():
    sc.card_stop()  # 立即停止


def cmd_run():
    global point_data
    for index in range(0, 5):
        if is_natural_num(getattr(ui, 'lineEdit_axis%s' % index).text()):
            point_data['axis'][index] = getattr(ui, 'lineEdit_axis%s' % index).text()
        if is_natural_num(getattr(ui, 'lineEdit_speed%s' % index).text()):
            point_data['speed'][index][0] = getattr(ui, 'lineEdit_speed%s' % index).text()
        if is_natural_num(getattr(ui, 'lineEdit_delay%s' % index).text()):
            point_data['delay'][index] = getattr(ui, 'lineEdit_delay%s' % index).text()
    PlanCmd_Thread.run_flg = True


def keyboard_release(key):
    global flg_key_run
    if ui.checkBox_key.isChecked() and flg_start['card']:
        try:
            if key == key.up:
                print('前')

                flg_key_run = True

                pValue[1] = pValue[1] + 30000 * int(five_key[1])
                if pValue[1] <= 0:
                    pValue[1] = 0
                ui.lineEdit_axis1.setText(str(pValue[1]))
                sc.card_setpos(2, pValue[1])
                sc.card_update()

            if key == key.down:
                print('后')

                flg_key_run = True

                pValue[1] = pValue[1] - 30000 * int(five_key[1])
                if pValue[1] <= 0:
                    pValue[1] = 0
                ui.lineEdit_axis1.setText(str(pValue[1]))
                sc.card_setpos(2, pValue[1])
                sc.card_update()

            if key == key.left:
                print('左')

                flg_key_run = True

                pValue[0] = pValue[0] - 30000 * int(five_key[0])
                if pValue[0] <= 0:
                    pValue[0] = 0
                ui.lineEdit_axis0.setText(str(pValue[0]))
                sc.card_setpos(1, pValue[0])
                sc.card_update()

            if key == key.right:
                print('右')

                flg_key_run = True

                pValue[0] = pValue[0] + 30000 * int(five_key[0])
                if pValue[0] <= 0:
                    pValue[0] = 0
                ui.lineEdit_axis0.setText(str(pValue[0]))
                sc.card_setpos(1, pValue[0])
                sc.card_update()

            if key == key.insert:
                print('上')

                flg_key_run = True

                pValue[2] = pValue[2] - 30000 * int(five_key[2])
                if pValue[2] <= 0:
                    pValue[2] = 0
                ui.lineEdit_axis2.setText(str(pValue[2]))
                sc.card_setpos(3, pValue[2])
                sc.card_update()

            if key == key.delete:
                print('下')

                flg_key_run = True

                pValue[2] = pValue[2] + 30000 * int(five_key[2])
                if pValue[2] <= 0:
                    pValue[2] = 0
                ui.lineEdit_axis2.setText(str(pValue[2]))
                sc.card_setpos(3, pValue[2])
                sc.card_update()

            if key == key.home:
                print('头左')

                flg_key_run = True

                pValue[3] = pValue[3] - 30000 * int(five_key[3])
                ui.lineEdit_axis3.setText(str(pValue[3]))
                sc.card_setpos(4, pValue[3])
                sc.card_update()

            if key == key.end:
                print('头右')

                flg_key_run = True

                pValue[3] = pValue[3] + 30000 * int(five_key[3])
                ui.lineEdit_axis3.setText(str(pValue[3]))
                sc.card_setpos(4, pValue[3])
                sc.card_update()

            if key == key.page_up:
                print('头上')

                flg_key_run = True

                pValue[4] = pValue[4] + 30000 * int(five_key[4])
                ui.lineEdit_axis4.setText(str(pValue[4]))
                sc.card_setpos(5, pValue[4])
                sc.card_update()

            if key == key.page_down:
                print('头下')

                flg_key_run = True

                pValue[4] = pValue[4] - 30000 * int(five_key[4])
                ui.lineEdit_axis4.setText(str(pValue[4]))
                sc.card_setpos(5, pValue[4])
                sc.card_update()

        except AttributeError:
            pass
            # print(key)


def keyboard_press(key):
    global flg_key_run
    try:
        if key == key.enter:
            cmd_stop()
    except:
        pass
    if ui.checkBox_key.isChecked() and flg_start['card']:
        try:
            Pos_Thread.run_flg = True
            if key == key.up:
                if flg_key_run:
                    print('前')

                    pos = 2000000 * int(five_key[1])
                    if pos <= 0:
                        pos = 0
                    sc.card_move(2, pos=pos)
                    sc.card_update()
                    flg_key_run = False
            elif key == key.down:
                if flg_key_run:
                    print('后')

                    pos = -2000000 * int(five_key[1])
                    if pos <= 0:
                        pos = 0
                    sc.card_move(2, pos=pos)
                    sc.card_update()
                    flg_key_run = False
            elif key == key.left:
                if flg_key_run:
                    print('左')

                    pos = -2000000 * int(five_key[0])
                    if pos <= 0:
                        pos = 0
                    sc.card_move(1, pos=pos)
                    sc.card_update()
                    flg_key_run = False
            elif key == key.right:
                if flg_key_run:
                    print('右')

                    pos = 2000000 * int(five_key[0])
                    if pos <= 0:
                        pos = 0
                    sc.card_move(1, pos=pos)
                    sc.card_update()
                    flg_key_run = False
            elif key == key.insert:
                if flg_key_run:
                    print('上')

                    pos = -2000000 * int(five_key[2])
                    if pos <= 0:
                        pos = 0
                    sc.card_move(3, pos=pos)
                    sc.card_update()
                    flg_key_run = False
            elif key == key.delete:
                if flg_key_run:
                    print('下')

                    pos = 2000000 * int(five_key[2])
                    if pos <= 0:
                        pos = 0
                    sc.card_move(3, pos=pos)
                    sc.card_update()
                    flg_key_run = False
            elif key == key.home:
                if flg_key_run:
                    print('头左')

                    sc.card_move(4, pos=-2000000 * int(five_key[3]), vel=50)
                    sc.card_update()
                    flg_key_run = False
            elif key == key.end:
                if flg_key_run:
                    print('头右')

                    sc.card_move(4, pos=2000000 * int(five_key[3]), vel=50)
                    sc.card_update()
                    flg_key_run = False
            elif key == key.page_up:
                if flg_key_run:
                    print('头下')

                    sc.card_move(5, pos=2000000 * int(five_key[4]), vel=50)
                    sc.card_update()
                    flg_key_run = False
            elif key == key.page_down:
                if flg_key_run:
                    print('头上')

                    sc.card_move(5, pos=-2000000 * int(five_key[4]), vel=50)
                    sc.card_update()
                    flg_key_run = False
        except AttributeError:
            # print(key)
            pass


class PosThread(QThread):
    """
    PosThread(QThread) 检测各轴位置
    """
    _signal = Signal(object)

    def __init__(self):
        super(PosThread, self).__init__()
        self.run_flg = True
        self.running = True

    def stop(self):
        self.run_flg = False
        self.running = False  # 修改标志位，线程优雅退出
        self.quit()  # 退出线程事件循环

    def run(self) -> None:
        global pValue
        while self.running:
            time.sleep(0.2)
            if not self.run_flg:
                continue
            if flg_start['card']:
                try:
                    for i in range(0, 5):
                        (res, pValue[i], pClock) = sc.get_pos(i + 1)
                    self._signal.emit(pValue)

                except:
                    pass
            # self.run_flg = False


def pos_signal_accept(msg):
    try:
        if len(msg) == 5 and not ui.checkBox_point.isChecked():
            for i in range(0, len(msg)):
                if getattr(ui, 'lineEdit_axis%s' % i).text() != str(msg[i]):
                    getattr(ui, 'lineEdit_axis%s' % i).setText(str(msg[i]))
        else:
            pass
    except:
        print("轴数据显示错误！")


class CardStartThread(QThread):
    """
        运动卡开启线程
    """
    _signal = Signal(object)

    def __init__(self):
        super(CardStartThread, self).__init__()
        self.run_flg = False
        self.running = True

    def stop(self):
        self.run_flg = False
        self.running = False  # 修改标志位，线程优雅退出
        self.quit()  # 退出线程事件循环

    def run(self) -> None:
        global flg_start
        card_num = ui.lineEdit_CardNo.text()
        if card_num.isdigit() and not (flg_start['card']):
            res = sc.card_open(int(card_num))
            print(res)
            if res == 0:
                Axis_Thread.run_flg = True  # 轴复位
                self._signal.emit(succeed('启动板卡：%s' % card_res[res]))
            else:
                self._signal.emit(fail('板卡链接失败：%s' % card_res[res]))
        else:
            self._signal.emit(fail('运动卡已链接~！'))


def CardStart_signal_accept(msg):
    ui.textBrowser.append(msg)
    scroll_to_bottom(ui.textBrowser)


# 滚动到 textBrowser 末尾
def scroll_to_bottom(text_browser: QTextBrowser):
    # 获取 QTextCursor 并移动到文档结尾
    cursor = text_browser.textCursor()
    cursor.movePosition(QTextCursor.MoveOperation.End)
    text_browser.setTextCursor(cursor)
    text_browser.ensureCursorVisible()


class AxisThread(QThread):
    """
    AxisThread(QThread) 轴复位线程
    """

    _signal = Signal(object)

    def __init__(self):
        super(AxisThread, self).__init__()
        self.run_flg = False
        self.running = True

    def stop(self):
        self.run_flg = False
        self.running = False  # 修改标志位，线程优雅退出
        self.quit()  # 退出线程事件循环

    def run(self) -> None:
        global flg_start
        while self.running:
            time.sleep(1)
            if not self.run_flg:
                continue
            print('串口运行')
            try:
                self._signal.emit(succeed('轴复位开始...'))
                nAxisList = [bytes.fromhex('01030B07000277EE'),
                             bytes.fromhex('02030B07000277DD'),
                             bytes.fromhex('03030B070002760C'),
                             bytes.fromhex('04030B07000277BB'),
                             bytes.fromhex('05030B070002766A')]
                for nAxis in nAxisList:
                    s485_data = s485.get_axis_pos(nAxis)
                    # print(s485_data)
                    if s485_data != 0:
                        s485_data['highPos'] = s485_data['highPos'] * five_axis[s485_data['nAxisNum'] - 1]
                        res = sc.GASetPrfPos(s485_data['nAxisNum'], s485_data['highPos'])
                        if res == 0:
                            self._signal.emit(succeed('%s 轴复位完成！' % s485_data['nAxisNum']))
                            flg_start['card'] = True
                        flg_start['s485'] = True
                    else:
                        flg_start['s485'] = False
                        flg_start['card'] = False
                        self._signal.emit(fail('复位串口未连接！'))
                self._signal.emit(succeed('轴复位完成！'))
            except:
                print("轴复位出错！")
                flg_start['s485'] = False
                self._signal.emit(fail('轴复位出错！'))
            self.run_flg = False


def Axis_signal_accept(msg):
    # print(message)
    try:
        if '轴复位完成！' == msg:
            time.sleep(0.2)
            for index in range(0, 5):
                point_data['axis'][index] = str(pValue[index])
        ui.textBrowser.append(str(msg))
        scroll_to_bottom(ui.textBrowser)
    except:
        print("运行数据处理出错！")


class SocketThread(QThread):
    """
    SocketThread(QThread) 获取动作线程
    """

    _signal = Signal(object)

    def __init__(self):
        super().__init__()
        self.run_flg = True
        self.running = True

    def stop(self):
        self.run_flg = False
        self.running = False  # 修改标志位，线程优雅退出
        self.quit()  # 退出线程事件循环

    def run(self) -> None:
        global flg_start
        global client_socket
        message = '{y@0}'
        response = '{yj0}'
        while self.running:
            time.sleep(2)
            if not self.run_flg:
                continue
            try:
                # 持续与服务器交互
                while self.run_flg:
                    if cmd_flag() or ('{yd' not in response):
                        # 发送数据到服务器
                        client_socket.sendall(message.encode("gbk"))
                        print(f"已发送数据: {message}")

                        response = client_socket.recv(1024).decode("gbk", errors="ignore")

                        self._signal.emit(response)
                        print(f"服务器响应: {response}")
                        message = data_split(response)
                    time.sleep(0.2)

            except ConnectionError as e:
                print(f"连接失败: {e}")
            finally:
                client_socket.close()
                self._signal.emit(fail("已关闭连接"))
                print("已关闭连接")


def Socket_signal_accept(msg):
    try:
        if '{yj1}' == msg:
            ui.checkBox_key.setChecked(True)
        elif '{yj0}' == msg:
            ui.checkBox_key.setChecked(False)
        ui.textBrowser.append(str(msg))
        scroll_to_bottom(ui.textBrowser)
    except:
        print("运行数据处理出错！")


def cmd_flag():
    res = True
    for index in range(2):
        if abs(int(point_data['axis'][index]) - pValue[index]) > 5000:
            res = False
    return res


def data_split(data):
    global point_data
    result = data.split("|")

    res_num = len(result) - 1

    position = result[0].find('{yd')
    if position != -1:
        result[0] = result[0][position + 3:]
        data_axis = result[0: 5]
        point_data['axis'] = data_axis
        position = result[res_num].find('}')
        if position != -1:
            result[res_num] = result[res_num][0:position]
        data_speed = result[res_num].split(",")
        for index, item in enumerate(data_speed):
            if index < 5:
                data_speed[index] = item.split("#")
                point_data['delay'][index] = data_speed[index][0]
                if not point_data['delay'][index].isdigit():
                    point_data['delay'][index] = '0'
                else:
                    point_data['delay'][index] = str(float(point_data['delay'][index]) / 1000)
                point_data['speed'][index] = data_speed[index][1:]
                for j, j_item in enumerate(point_data['speed'][index]):
                    if j_item == '':
                        point_data['speed'][index][j] = '0'
                    if point_data['speed'][index][0] == '0':
                        point_data['speed'][index][0] = result[5]
                    if point_data['speed'][index][1] == '0':
                        point_data['speed'][index][1] = result[6]
                    if point_data['speed'][index][2] == '0':
                        point_data['speed'][index][2] = result[7]
        # print(point_data)
        PlanCmd_Thread.run_flg = True
        return '{yq}'
    if '{yy' in data:
        return '{yy%s,%s,%s,%s,%s}' % (str(pValue[0]), str(pValue[1]), str(pValue[2]), str(pValue[3]), str(pValue[4]))
    elif '{y3' in data:
        return '%s@%s|%s|%s|%s|%s}' % (
            data[0:-1], str(pValue[0]), str(pValue[1]), str(pValue[2]), str(pValue[3]), str(pValue[4]))
    elif '{y2' in data:
        position = data.find('|')
        position_end = data.find('}')
        if position != -1 and position_end != -1:
            name = data[position + 1: position_end]
            switch = data[3: position]
            print(name, switch)
            for Voltage_index, Voltage_item in enumerate(Voltage_list):
                print('打开', name, switch)
                if name == Voltage_item:
                    sw = 1 if switch == '0' else 0
                    sc.GASetExtDoBit(Voltage_index, sw)
                    time.sleep(0.1)
                    return '{y2}'
    return '{yq}'


class PlanCmdThread(QThread):
    """
    CmdThread(QThread) 执行运动方案线程
    """
    _signal = Signal(object)

    def __init__(self):
        super(PlanCmdThread, self).__init__()
        self.run_flg = False
        self.cmd_next = False
        self.running = True

    def stop(self):
        self.run_flg = False
        self.running = False  # 修改标志位，线程优雅退出
        self.quit()  # 退出线程事件循环

    def run(self) -> None:
        axis_list = [1, 2, 4, 8, 16]
        while self.running:
            time.sleep(0.1)
            if not self.run_flg:
                continue

            if flg_start['card']:
                self.cmd_next = False  # 初始化手动快速跳过下一步动作标志
                try:
                    # 轴运动
                    axis_bit = 0  # 非延迟轴统计
                    max_delay_time = 0  # 记录最大延迟时间
                    delay_list = []  # 延迟的轴列表
                    for index in range(0, 5):
                        axis_item = point_data['axis'][index]
                        if float(axis_item) < 0 and (index in [0, 1]):
                            axis_item = '0'
                        speed_item = point_data['speed'][index]
                        delay_item = point_data['delay'][index]
                        print(axis_item, speed_item, delay_item)
                        sc.card_move(index + 1, int(float(axis_item)),
                                     vel=abs(int(float(speed_item[0]))),
                                     dAcc=float(speed_item[1]),
                                     dDec=float(speed_item[2]),
                                     dVelStart=float(speed_item[3]),
                                     dSmoothTime=int(float(speed_item[4]))
                                     )
                        if float(delay_item) == 0:
                            axis_bit += axis_list[index]
                        else:
                            delay_list.append([axis_list[index], float(format(float(delay_item), ".3f"))])
                        if max_delay_time < float(format(float(delay_item), ".3f")):
                            max_delay_time = float(format(float(delay_item), ".3f"))
                    list_equal = {}
                    for index in range(len(delay_list)):
                        if not (delay_list[index][1] in list_equal.keys()):
                            list_equal[delay_list[index][1]] = delay_list[index][0]
                        else:
                            list_equal[delay_list[index][1]] += delay_list[index][0]
                    delay_list = []
                    for key in list_equal.keys():
                        delay_list.append([list_equal[key], key])
                    if axis_bit != 0:  # 非延迟轴
                        res = sc.card_update(axis_bit)
                        if res != 0:
                            print("运动板通信出错！")
                            flg_start['card'] = False
                            self._signal.emit(fail("运动板通信出错！"))
                    old_time = 0
                    for t in range(0, int(max_delay_time * 100) + 1):  # 延迟轴
                        for index in range(len(delay_list)):
                            if t >= delay_list[index][1] * 100 > old_time:
                                sc.card_update(delay_list[index][0])
                                old_time = t
                        time.sleep(0.01)
                    print('动作已完成！')
                except:
                    print("运动板运行出错！")
                    self._signal.emit(fail("运动板通信出错！"))
                if not flg_start['card']:
                    self._signal.emit(fail("运动卡未链接！"))
            self.run_flg = False


def Cmd_signal_accept(msg):
    # print(message)
    try:
        ui.textBrowser.append(str(msg))
        scroll_to_bottom(ui.textBrowser)
    except:
        print("运行数据处理出错！")


class PlanBallNumThread(QThread):
    """
    PlanBallNumThread(QThread) 摄像头运动方案线程
    """
    _signal = Signal(object)

    def __init__(self):
        super(PlanBallNumThread, self).__init__()
        self.run_flg = True
        self.running = True

    def stop(self):
        self.run_flg = False
        self.running = False  # 修改标志位，线程优雅退出
        self.quit()  # 退出线程事件循环

    def run(self) -> None:
        global flg_start
        while self.running:
            time.sleep(0.1)
            if (not self.run_flg) or (not flg_start['card']):
                continue
            print('正在接收运动卡输入信息！')
            try:
                res = sc.GASetDiReverseCount()  # 输入次数归0
                res1 = sc.GASetDiReverseCount(diIndex=1)  # 输入次数归0
                num_old = 0
                num_old1 = 0
                if res == 0 and res1 == 0:
                    while self.run_flg:
                        res, value = sc.GAGetDiReverseCount()
                        # print(res, value)
                        if res == 0:
                            num = int(value[0] / 2)
                            if num != num_old:
                                num_old = num
                                # 发送数据到服务器
                                client_socket.sendall('{y4}'.encode("gbk"))
                                self._signal.emit(str(num))
                                print(num)
                            if num >= balls_count:
                                res = sc.GASetDiReverseCount()  # 输入次数归0
                        else:
                            flg_start['card'] = False
                            self._signal.emit(fail("运动板x输入通信出错！"))
                            break

                        res1, value1 = sc.GAGetDiReverseCount(diIndex=1)
                        if res1 == 0:
                            num1 = int(value1[0] / 2)
                            if num1 != num_old1:
                                num_old1 = num1
                                # 发送数据到服务器
                                client_socket.sendall('{y9}'.encode("gbk"))
                                self._signal.emit(str(num1))
                                print(num1)
                            if num1 >= balls_count:
                                res1 = sc.GASetDiReverseCount(diIndex=1)  # 输入次数归0
                        else:
                            flg_start['card'] = False
                            self._signal.emit(fail("运动板x输入通信出错！"))
                            break
                        time.sleep(0.01)
                else:
                    print("次数归0 失败！")
                    flg_start['card'] = False
                    self._signal.emit(fail("运动板x输入通信出错！"))
            except:
                print("接收运动卡输入 运行出错！")
                flg_start['card'] = False
                self._signal.emit(fail("运动板x输入通信出错！"))
            # self.run_flg = False


def PlanBallNum_signal_accept(msg):
    ui.textBrowser.append(msg)
    scroll_to_bottom(ui.textBrowser)


def load_main_yaml():
    global balls_count
    global five_axis
    global five_key
    global Voltage_list
    file = "main_config.yml"
    if os.path.exists(file):
        f = open(file, 'r', encoding='utf-8')
        main_all = yaml.safe_load(f)
        f.close()

        ui.lineEdit_five_axis.setText(str(main_all['five_axis']))
        ui.lineEdit_five_key.setText(str(main_all['five_key']))
        # 赋值变量
        balls_count = abs(int(float(main_all['balls_count'])))
        five_axis = main_all['five_axis']
        five_key = main_all['five_key']
    else:
        print("文件不存在")
    try:
        voltage, ports = query_sql()  # 16个电压输出
        print(voltage)
        print(ports)
        for i, key in enumerate(voltage.keys()):
            Voltage_list[i] = voltage[key]
        for i, key in enumerate(ports.keys()):
            if key == '全局配置.IP':
                position = ports[key].rfind(".")
                ui.lineEdit_CardNo.setText(ports[key][position + 1:])
            elif key == '全局配置.驱动器端口':
                ui.lineEdit_s485_Axis_No.setText(ports[key])
                s485.s485_Axis_No = 'COM%s' % ports[key]
    except:
        ui.textBrowser.append('机关数据获取失败！')
        print('机关数据获取失败！')


def save_main_yaml():
    global five_axis
    global five_key

    file = "main_config.yml"
    if os.path.exists(file):
        try:
            with (open(file, "r", encoding="utf-8") as f):
                main_all = yaml.safe_load(f)
                # print(main_all)
                main_all['five_axis'] = eval(ui.lineEdit_five_axis.text())
                main_all['five_key'] = eval(ui.lineEdit_five_key.text())

                # 赋值变量
                five_axis = main_all['five_axis']
                five_key = main_all['five_key']
            with open(file, "w", encoding="utf-8") as f:
                yaml.dump(main_all, f, allow_unicode=True)
            f.close()
            ui.textBrowser.append(succeed('方案保存：成功'))
        except:
            ui.textBrowser.append(fail('方案保存：失败'))
        print("保存成功~！")


class ZApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.aboutToQuit.connect(self.onAboutToQuit)

    @Slot()
    def onAboutToQuit(self):
        print("Exiting the application.")
        try:
            # 停止所有服务线程
            self.stop_all_threads()

        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Stopping application.")

        finally:
            print("Waiting for all threads to exit...")
            self.join_all_threads()
            print("All servers are closed. Exiting.")

    def stop_all_threads(self):
        """停止所有线程的函数。"""
        try:
            Axis_Thread.stop()
            Pos_Thread.stop()
            CardStart_Thread.stop()
            PlanCmd_Thread.stop()
            Socket_Thread.stop()
            PlanBallNum_Thread.stop()
        except Exception as e:
            print(f"Error stopping threads: {e}")

    def join_all_threads(self):
        """等待所有线程退出。"""
        try:
            Axis_Thread.wait()
            Pos_Thread.wait()
            CardStart_Thread.wait()
            PlanCmd_Thread.wait()
            Socket_Thread.wait()
            PlanBallNum_Thread.wait()
        except Exception as e:
            print(f"Error waiting threads: {e}")


class ZUi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, z_window):
        super().setupUi(z_window)
        # tb_camera = self.tableWidget_camera
        # tb_camera.horizontalHeader().setStyleSheet("QHeaderView::section{background:rgb(245,245,245);}")
        # tb_camera.verticalHeader().setStyleSheet("QHeaderView::section{background:rgb(245,245,245);}")


class ZMainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口图标
        self.setWindowIcon(QIcon("./icon.ico"))

    def closeEvent(self, event):
        # 创建确认对话框
        reply = QMessageBox.question(
            self,
            "退出",
            "您确定要退出程序吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        # 检查用户的响应
        if reply == QMessageBox.Yes:
            event.accept()  # 接受关闭事件，程序退出
        else:
            event.ignore()  # 忽略关闭事件，程序继续运行


if __name__ == '__main__':
    app = ZApp(sys.argv)

    z_window = ZMainwindow()
    ui = ZUi()
    ui.setupUi(z_window)
    z_window.show()

    sc = SportCard()  # 运动卡
    s485 = Serial485()  # 摄像头
    s485.s485_Axis_No = 'COM22'

    Voltage_list = ['一弹射', '起砸门', '', '终点', '机关1', '', '', '', '', '', '', '', '', '', '', '']
    load_main_yaml()
    # print(Voltage_list)

    balls_count = 8  # 运行球数
    balls_send = 0  # 发送球数据
    flg_key_run = True  # 键盘控制标志
    pValue = [0, 0, 0, 0, 0]  # 各轴位置
    five_key = [1, 1, 1, 1, -1]
    five_axis = [1, 1, 1, 1, -1]
    flg_start = {'card': False, 's485': False}  # 各硬件启动标志
    point_data = {'axis': ['0'] * 5,
                  'speed': [['100', '0.3', '0.2', '5', '1']] * 5,
                  'delay': ['0'] * 5}

    listener = pynput.keyboard.Listener(on_press=keyboard_press, on_release=keyboard_release)
    listener.start()  # 键盘监听线程 1

    Pos_Thread = PosThread()  # 实时监控各轴位置 8
    Pos_Thread._signal.connect(pos_signal_accept)
    Pos_Thread.start()

    CardStart_Thread = CardStartThread()  # 运动卡开启线程 12
    CardStart_Thread._signal.connect(CardStart_signal_accept)
    CardStart_Thread.start()

    Axis_Thread = AxisThread()  # 轴复位 7
    Axis_Thread._signal.connect(Axis_signal_accept)
    Axis_Thread.start()

    PlanCmd_Thread = PlanCmdThread()  # 总运行方案 2
    PlanCmd_Thread._signal.connect(Cmd_signal_accept)
    PlanCmd_Thread.start()

    # 目标服务器 IP 和端口
    server_ip = "127.0.0.1"  # 替换为实际服务器地址
    server_port = 19888
    # 创建 TCP 套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    client_socket.connect((server_ip, server_port))
    print(f"成功连接到服务器 {server_ip}:{server_port}")

    Socket_Thread = SocketThread()  # 轴复位 7
    Socket_Thread._signal.connect(Socket_signal_accept)
    Socket_Thread.start()

    PlanBallNum_Thread = PlanBallNumThread()  # 统计过终点的球数 5
    PlanBallNum_Thread._signal.connect(PlanBallNum_signal_accept)
    PlanBallNum_Thread.start()

    ui.pushButton_CardStart.clicked.connect(card_start)
    ui.pushButton_CardStop.clicked.connect(cmd_stop)
    ui.pushButton_CardReset.clicked.connect(card_reset)
    ui.pushButton_CardCloseAll.clicked.connect(card_close_all)
    ui.pushButton_CardRun.clicked.connect(cmd_run)

    ui.checkBox_shoot.checkStateChanged.connect(organ_shoot)
    ui.checkBox_start.checkStateChanged.connect(organ_start)
    ui.checkBox_end.checkStateChanged.connect(organ_end)
    ui.checkBox_switch.checkStateChanged.connect(organ_number)

    ui.lineEdit_five_key.editingFinished.connect(save_main_yaml)
    ui.lineEdit_five_axis.editingFinished.connect(save_main_yaml)

    sys.exit(app.exec())

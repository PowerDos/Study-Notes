import paho.mqtt.client as mqtt
import datetime
def mqttc(request):
    def on_connect(client, userdata, flags, rc):  # 连接后返回0为成功
        # print("Connected with result code " + str(rc))
        client.subscribe(topic, qos=1)  # qos

    flag = True
    info = ''
    def on_publish(msg, rc):  # 成功发布消息的操作
        if rc == 0:
            pass
            # print("publish success, msg = " + msg)

    def on_message(client, userdata, msg):
        global flag
        global info
        info = "topic:" + msg.topic + " Message:" + str(msg.payload.decode('utf-8'))
        # print("topic:" + msg.topic + " Message:" + str(msg.payload.decode('utf-8')))
        flag = False
        # return HttpResponse("topic:" + msg.topic + " Message:" + str(msg.payload.decode('utf-8')))

    trust = "D:/Python/PycharmProjects/mqtt-py/root_cert.pem"
    user = "cloudcoin/device"
    pwd = "fXRJqx1e9Iiq9MTadmeSkERwa0AC5GEV/F7HNtwFDcg="
    endpoint = "cloudcoin.mqtt.iot.gz.baidubce.com"
    port = 1884
    topic = "one2one/thing02"

    client = mqtt.Client(
        client_id="test_mqtt_receiver_1",  # 用来标识设备的ID，用户可自己定义，在同一个实例下，每个实体设备需要有一个唯一的ID
        clean_session=True,
        userdata=None,
        protocol='MQTTv31'
    )


    client.tls_insecure_set(True)  # 检查hostname的cert认证
    client.tls_set(trust)  # 设置认证文件
    client.username_pw_set(user, pwd)  # 设置用户名，密码
    client.on_connect = on_connect  # 连接后的操作
    client.on_message = on_message  # 接受消息的操作
    client.connect(endpoint, port, 60)  # 连接服务 keepalive=60
    client.loop_start()
    # client.loop_start()
    msg = "send the message at " + str(datetime.datetime.now())
    rc, mid = client.publish("one2one/server", payload=msg, qos=1)  # qos
    on_publish(msg, rc)

    while flag:
        # print(flag)
        client.loop_start()

    return HttpResponse(info)
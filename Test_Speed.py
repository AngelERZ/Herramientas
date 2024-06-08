import speedtest_cli as speedtest

def test_internet_speed():
    try:
        st = speedtest.Speedtest()
        print("Probando la velocidad de internet...")

        download_speed = st.download() / 1000000
        upload_speed = st.upload() / 1000000

        print("Velocidad de descarga: {:.2f} Mbps"
             .format(download_speed))
        print("Velocidad de subida: {:.2f} Mbps"
             .format(upload_speed))
        
    except speedtest.SpeedtestException as e:
        print("Error al probar la velocidad de internet:", 
              "la prueba de velocidad:", str(e))

test_internet_speed()

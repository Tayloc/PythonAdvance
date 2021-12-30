"""
原理：将一组简单数据进行打包，转换为bytes格式发送。或者将一组bytes格式数据，进行解析。
接口使用
    st = struct.Struct(fmt)
        功能：生成结构化对象
        参数：fmt 定制的数据结构

    st.pack(v1, v2, v3...)
        功能：将一组数据按照指定格式打包转换为bytes
        参数：要打包的数据
        返回值：bytes字节串

    st.unpack(bytes_data)
        功能：将bytes字节串按照指定的格式解析
        参数：要解析的字节串
        返回值：解析后的内容

直接使用struct模块调用pack和unpack,此时这两个函数第一个参数传入fmt.其他用法功能相同
    struct.pack(fmt, v1, v2, v3...)
    struct.unpack(fmt, bytes_data)
"""

import struct

# 生成结构化对象
st = struct.Struct('i4sf')

# 将一组数据打包成bytes格式
data = st.pack(1, b'Lily', 2.0)

# 将bytes字节串按照指定格式解析
print(st.unpack(data))

data = struct.pack('i4sf', 1, b'Lucy', 1.70)
print(data)
print(struct.unpack('i4sf', data))

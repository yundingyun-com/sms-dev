# 示例：如何使用 python 实现自动发送短信

## 0. 前置条件

使用此文档，默认已拥有完善的python开发环境。

## 1. 安装SDK包

本平台兼容阿里云 python sdk ，详细说明请见[官方文档](https://help.aliyun.com/document_detail/112147.html?spm=a2c4g.11186623.6.645.59de5f30Cp3u3n)。可以通过以下两种方式安装Python SDK。

* 使用依赖包工具安装（推荐）
* 自行下载安装

### 1.1 使用依赖包工具安装（推荐）

执行以下命令，安装阿里云SDK核心库：

```bash
pip install aliyun-python-sdk-core
```

在安装完成后，您可以使用[OpenAPI Explorer](https://api.aliyun.com/?spm=a2c4g.11186623.2.15.57c059ad3QlmqO#/?product=Dysmsapi&lang=PYTHON)来生成相关API的Demo并应用在所需的项目中。

### 1.2 自行下载安装

使用git clone或其它手段下载aliyun-python-sdk-core并自行添加解决方案。

aliyun-python-sdk-core GitHub地址：[aliyun-python-sdk-core](https://github.com/aliyun/aliyun-openapi-python-sdk/tree/master/aliyun-python-sdk-core?spm=a2c4g.11186623.2.16.57c059ad3QlmqO)。

在安装完成后，可以使用[OpenAPI Explorer](https://api.aliyun.com/?spm=a2c4g.11186623.2.15.57c059ad3QlmqO#/?product=Dysmsapi&lang=PYTHON)来生成相关API的Demo并应用在所需的项目中。

## 2. SDK包代码的变动

将此[/aliyunsdkcore/auth/composer/rpc_signature_composer.py](https://github.com/aliyun/aliyun-openapi-python-sdk/blob/master/aliyun-python-sdk-core/aliyunsdkcore/auth/composer/rpc_signature_composer.py)，第43行注释掉。
> #parameters["SignatureType"] = signer.get_signer_type()

示例如下：

```python
    if 'Signature' in parameters:
        del parameters['Signature']
    parameters["Timestamp"] = helper.get_iso_8061_date()
    parameters["SignatureMethod"] = signer.get_signer_name()
    #parameters["SignatureType"] = signer.get_signer_type()
    parameters["SignatureVersion"] = signer.get_signer_version()
    parameters["SignatureNonce"] = helper.get_uuid()
    parameters["AccessKeyId"] = access_key_id
```

## 3. 示例代码使用步骤

1.打开示例代码sms.py，并修改SendSms文件下的发送参数以及API地址。
2.运行示例代码

## 4. 参考信息

阿里云 SDK 频道：[https://develop.aliyun.com/tools/sdk?#/python](https://develop.aliyun.com/tools/sdk?#/python)
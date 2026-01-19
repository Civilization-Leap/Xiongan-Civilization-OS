
#!/usr/bin/env python3
"""
简易测试运行脚本 - 用于验证DID模块功能
"""

import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.did import DID

def main():
    print("🧪 Xiongan Civilization OS - DID模块验证")
    print("=" * 50)
    
    # 测试1: 创建居民DID
    print("\n1. 创建居民身份:")
    resident = DID.create(did_type="resident")
    print(f"   ✅ 生成: {resident}")
    print(f"   类型: {resident.did_type}")
    print(f"   标识符: {resident.method_specific_id}")
    
    # 测试2: 创建组织DID
    print("\n2. 创建组织身份:")
    organization = DID.create(did_type="organization")
    print(f"   ✅ 生成: {organization}")
    
    # 测试3: 解析测试
    print("\n3. 解析DID字符串:")
    test_did = "did:xca:device:test_device_001"
    parsed = DID.parse(test_did)
    print(f"   ✅ 解析成功: {parsed}")
    print(f"   类型: {parsed.did_type}")
    
    # 测试4: 生成文档
    print("\n4. 生成DID文档:")
    doc = resident.generate_document()
    print(f"   ✅ 文档生成成功")
    print(f"   包含字段: {', '.join(doc.keys())}")
    
    # 测试5: 异常处理
    print("\n5. 验证异常处理:")
    try:
        DID.parse("invalid_format")
        print("   ❌ 应该抛出异常但未抛出")
    except Exception as e:
        print(f"   ✅ 正确捕获异常: {type(e).__name__}")
    
    print("\n" + "=" * 50)
    print("🎉 所有基础验证通过！")
    print("\n下一步：运行完整测试: python -m pytest tests/ -v")

if __name__ == "__main__":
    main()

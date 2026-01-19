
#!/usr/bin/env python3
"""
Xiongan Civilization OS - DID模块演示
临时验证脚本，绕过导入问题
"""

import sys
import os

# 手动添加src目录到路径
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "src")
sys.path.insert(0, src_path)

print("🚀 Xiongan Civilization OS - DID模块验证")
print("=" * 60)

try:
    # 尝试导入DID模块
    from core.did import DID
    from core.exceptions import DIDValidationError
    
    print("✅ 模块导入成功")
    
    # 演示1: 创建居民DID
    print("\n1. 创建雄安新区居民数字身份:")
    resident_did = DID.create(did_type="resident")
    print(f"   🔹 DID: {resident_did}")
    print(f"   类型: {resident_did.did_type}")
    print(f"   标识符: {resident_did.method_specific_id}")
    
    # 演示2: 创建组织DID
    print("\n2. 创建组织身份:")
    org_did = DID.create(did_type="organization")
    print(f"   🔹 DID: {org_did}")
    
    # 演示3: 解析DID
    print("\n3. 解析DID字符串:")
    test_str = "did:xca:device:smart_sensor_001"
    parsed_did = DID.parse(test_str)
    print(f"   解析 '{test_str}'")
    print(f"   🔹 类型: {parsed_did.did_type}")
    print(f"   🔹 标识符: {parsed_did.method_specific_id}")
    
    # 演示4: 生成DID文档
    print("\n4. 生成居民DID文档:")
    doc = resident_did.generate_document()
    print(f"   🔹 文档ID: {doc['id']}")
    print(f"   🔹 创建时间: {doc['created']}")
    print(f"   🔹 验证方法: {len(doc['verificationMethod'])} 个")
    
    # 演示5: 异常处理
    print("\n5. 验证错误处理:")
    try:
        DID.parse("not_a_valid_did")
    except DIDValidationError as e:
        print(f"   🔹 正确捕获异常: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 DID模块核心功能验证通过！")
    print("\n下一步: 运行完整测试: python -m pytest")
    
except ImportError as e:
    print(f"❌ 导入失败: {e}")
    print("\n可能的原因:")
    print("1. 缺少 src/__init__.py 文件")
    print("2. Python路径设置不正确")
    print("\n请先创建 src/__init__.py 文件")
except Exception as e:
    print(f"❌ 运行时错误: {type(e).__name__}: {e}")


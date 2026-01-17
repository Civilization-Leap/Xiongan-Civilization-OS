`python
   #!/usr/bin/env python3
   # 简易验证脚本 - 测试DID核心功能
   
   import sys
   sys.path.insert(0, 'src')
   
   from core.did import DID
   
   print("=== Xiongan Civilization OS - DID模块验证 ===")
   
   # 测试1: 创建DID
   print("\n1. 创建新的居民DID:")
   resident_did = DID.create(did_type="resident")
   print(f"   生成: {resident_did}")
   
   # 测试2: 解析DID
   print("\n2. 解析DID字符串:")
   test_did_str = "did:xca:device:test123"
   parsed_did = DID.parse(test_did_str)
   print(f"   解析 '{test_did_str}' -> 类型: {parsed_did.did_type}")
   
   # 测试3: 生成DID文档
   print("\n3. 生成DID文档:")
   doc = resident_did.generate_document()
   print(f"   文档ID: {doc['id']}")
   print(f"   创建时间: {doc['created']}")
   print(f"   验证方法: {len(doc['verificationMethod'])} 个")
   
   print("\n✅ 基本功能验证通过！")

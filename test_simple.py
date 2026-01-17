
#!/usr/bin/env python3
"""
简单测试脚本 - 绕过导入问题直接测试
"""

import sys
import os

# 直接添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("🧪 简单DID功能测试")
print("=" * 40)

try:
    # 直接导入did模块
    from core.did import DID
    
    print("✅ 直接导入成功")
    
    # 测试基本功能
    did = DID.create(did_type="test")
    print(f"✅ 创建DID: {did}")
    
    # 测试解析
    test_str = "did:xca:device:test123"
    parsed = DID.parse(test_str)
    print(f"✅ 解析DID: {parsed}")
    
    # 测试文档生成
    doc = did.generate_document()
    print(f"✅ 生成文档: {doc['id']}")
    
    print("\n" + "=" * 40)
    print("🎉 所有基本功能正常！")
    
except Exception as e:
    print(f"❌ 错误: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
```

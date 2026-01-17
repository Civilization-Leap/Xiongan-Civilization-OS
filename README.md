# Xiongan-Civilization-OS
雄安“文明跃迁验证试验区”的顶层设计承载着破解城市发展困境、探索未来文明形态的历史使命。试验区不仅是物理空间的建设，更是制度规则与文明范式的创新实践。其战略定位锚定全球视野，核心原则贯穿系统思维，共同构成未来城市可持续发展的底层逻辑。这一设计聚焦人类城市文明演进的共性难题，通过制度创新与技术赋能的深度融合，构建具有示范意义的城市发展新范式。
## 🆔 核心模块：去中心化身份 (DID)

我们已实现符合W3C标准的去中心化身份系统，这是文明操作系统的信任基石。

### 快速使用

```python
from src.core.did import DID

# 1. 创建雄安新区居民数字身份
resident = DID.create(did_type="resident")
print(f"居民DID: {resident}")

# 2. 解析已有DID
parsed = DID.parse("did:xca:organization:foundation_001")
print(f"类型: {parsed.did_type}")

# 3. 生成身份文档
doc = resident.generate_document()
```

DID格式

```
did:xca:<类型>:<唯一标识符>
```

· 方法: xca (Xiongan Civilization OS)
· 类型: resident(居民), organization(组织), device(设备), service(服务)
· 标识符: 32字符哈希值
```markdown
## 🧪 运行测试

### 快速验证
```bash
# 运行简易验证脚本
python run_tests.py

# 运行完整测试
pip install pytest
python -m pytest tests/ -v
```

开发环境设置

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest
```

## License
  Licensed under the Apache License, Version 2.0. Copyright 2024 [ZhongXinWang].

Created: 2026-06-10 10:00
#note

Software engineering patterns are reusable structural solutions to recurring problems in production codebases. For ML engineers who learned programming primarily through data work and modelling, these patterns can feel abstract — but most have direct analogies in the ML tooling already in daily use. This note covers eleven patterns that appear frequently in production Python systems.

## Structural Patterns

### Protocol (Interface)
A **Protocol** defines a set of method signatures that any class may satisfy structurally, without inheritance. This formalises duck typing. The sklearn API is the canonical ML analogy: `RandomForestClassifier`, `LogisticRegression`, and `SVC` all expose `.fit()`, `.predict()`, and `.score()`, allowing any of them to slot into a `Pipeline` without changing the pipeline code. Python's `typing.Protocol` captures this contract statically. Use when two or more implementations of the same concept exist, or when testing requires a lightweight fake. Avoid for single-use concrete classes — the abstraction adds no value.

### Hexagonal Architecture (Ports & Adapters)
Core business logic communicates with the outside world only through **ports** (abstract interfaces). Concrete integrations — S3, W&B, MLflow — live on the boundary as **adapters**. The training loop does not know whether it is writing to W&B or stdout; only the injected adapter knows. This lets the same core code run locally with lightweight fakes and in production with real cloud services — zero changes to the training logic itself. See [[Hexagonal Architecture]] for a deeper treatment in the context of agentic systems.

### Singleton
Ensures a single instance of a class exists for the lifetime of a process. Loading large model weights once at server startup and reusing that object across inference calls is a singleton in practice. Appropriate for expensive-to-create, shared resources (model weights, connection pools, API clients). Problematic when objects need independent state across concurrent workers — state leaks between tasks — and hard to test cleanly unless a reset mechanism is provided.

### Dependency Injection (DI)
Dependencies are passed in from outside rather than instantiated internally. Passing an `optimizer` argument to a `Trainer` rather than hardcoding `Adam` inside the constructor is dependency injection. The pattern decouples configuration from logic, enables testing with lightweight fakes, and makes swapping backends trivial. Watch for constructor bloat: if `__init__` accumulates more than four or five injected dependencies, the class boundary is probably wrong.

## Behavioural Patterns

### Decorator Pattern
A function that wraps another function to inject behaviour without modifying the original. `@torch.no_grad()` is the canonical ML example — gradient computation is disabled around an evaluation function without touching the function body. Best suited for cross-cutting concerns applied uniformly across many functions: timing, logging, retries, caching. If the wrapping logic is specific to one function, inline it. A decorator used once is indirection with no payoff.

### Context Manager Protocol
The `__enter__` / `__exit__` dunder pair guarantees teardown even when exceptions occur. The critical guarantee: `__exit__` always runs. PyTorch uses this pervasively — `with torch.no_grad():`, `with torch.cuda.amp.autocast():`, `tempfile.TemporaryDirectory()`. The pattern belongs wherever setup must be paired with cleanup: files, GPU memory, temporary directories, database connections, distributed locks.

### Error Isolation
Wrapping calls to secondary systems in `try/except` so failures in those systems cannot crash the primary process. If W&B is unreachable during a multi-day training run, the run should lose its dashboard, not its model. Apply exclusively to secondary concerns: logging, telemetry, caching. Silencing errors in primary logic — the model forward pass, the data pipeline — produces silent data corruption, which is the worst kind of bug.

### Graceful Degradation
A system designed to shed non-essential capabilities progressively rather than fail catastrophically. A model server might fall back from GPU inference → CPU inference → cached predictions → popular-item defaults, crashing only when the model file itself is absent. Avoid in safety-critical contexts where partial results are worse than hard failures — a half-computed feature vector fed to a model produces garbage outputs with no warning.

### Idempotency
An operation is **idempotent** if calling it once or many times produces the same effect. `model.eval()` in PyTorch is idempotent; `optimizer.step()` is not. In distributed systems, network failures and queue redelivery can cause operations to execute more than once; idempotency makes retries safe. Critical for cleanup methods, PUT/DELETE endpoints, and any handler that may be called from overlapping code paths.

## Concurrency and Import Patterns

### Context Variables (`contextvars`)
Thread-local-like storage that also works correctly across `async` tasks, with each task receiving an isolated copy of a variable. The ML analogy is PyTorch autograd: the computation graph propagates implicitly through the execution context without being passed as an explicit argument. Use for request-scoped state (trace IDs, user context) in async servers where threading a parameter through multiple call layers is impractical. In scripts without concurrency, a plain global is simpler and sufficient.

### Lazy Imports
Moving an `import` statement inside a function body so it executes only when that function is called. Practical for optional dependencies (plotting libraries absent on headless training servers), circular imports, and rarely-needed expensive modules. Core dependencies should remain at the module top level — lazy-importing them hides failures until runtime and makes the dependency graph harder to trace.

## References
1. [Clean Architecture](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/) — Robert C. Martin
2. [Architecture Patterns with Python](https://www.oreilly.com/library/view/architecture-patterns-with/9781492052197/) — Harry Percival & Bob Gregory
3. [Dependency Injection](https://martinfowler.com/articles/injection.html) — Martin Fowler
4. [contextvars — Python stdlib](https://docs.python.org/3/library/contextvars.html)

#### Tags
#python #software_engineering #mlops #patterns #dependency_injection

// src/infrastructure/database/InMemoryDatabase.ts
// Simulación de capa de acceso a datos.
export class InMemoryDatabase {
  private storage: Record<string, any[]> = {
    users: []
  }

  insert(table: string, item: any): void {
    if (!this.storage[table]) {
      this.storage[table] = []
    }
    this.storage[table].push(item)
  }

  findOne(table: string, predicate: (item: any) => boolean): any | null {
    const tableData = this.storage[table] ?? []
    return tableData.find(predicate) ?? null
  }
}

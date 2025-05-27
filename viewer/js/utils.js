export async function loadScale(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error('Failed to load scale file');
  return await res.json();
}

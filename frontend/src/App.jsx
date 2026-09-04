import { useState, useEffect } from 'react'
import ShopMap from './components/ShopMap.jsx'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default function App() {
  const [shops, setShops] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(`${API_URL}/shops`)
      .then((res) => {
        if (!res.ok) throw new Error(`Server error: ${res.status}`)
        return res.json()
      })
      .then((data) => {
        setShops(data)
        setLoading(false)
      })
      .catch((err) => {
        console.error(err)
        setError('Could not load shops. Is the backend running?')
        setLoading(false)
      })
  }, [])

  if (loading) {
    return <div className="status-screen">Loading shops…</div>
  }

  if (error) {
    return <div className="status-screen error">{error}</div>
  }

  return (
    <div className="app">
      <header className="header">
        <h1 className="header-title">Thrift Map</h1>
        <span className="header-count">
          {shops.length} {shops.length === 1 ? 'shop' : 'shops'} in Oslo
        </span>
      </header>
      <div className="map-wrapper">
        <ShopMap shops={shops} />
      </div>
    </div>
  )
}

/*
 *  triedatum.cc
 *
 *  This file is part of NEST.
 *
 *  Copyright (C) 2004 The NEST Initiative
 *
 *  NEST is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  NEST is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with NEST.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#include "triedatum.h"
#include "interpret.h"

sli::pool TrieDatum::memory( sizeof( TrieDatum ), 1024, 1 );

bool
TrieDatum::equals( Datum const* dat ) const
{
  // The following construct works around the problem, that
  // a direct dynamic_cast<const GenericDatum<D,slt> * > does not seem
  // to work.

  const TrieDatum* fd = dynamic_cast< TrieDatum* >( const_cast< Datum* >( dat ) );

  return ( fd == NULL ) ? false : ( tree == fd->tree );
}
